#python3 manage.py runapscheduler

import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.mail import mail_managers
from django.core.management.base import BaseCommand
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
import datetime
from django.core.mail import EmailMultiAlternatives

from news.models import Post, Category
from subscriptions.models import Subscription

logger = logging.getLogger(__name__)


def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    post = Post.objects.filter(date_creation__gte=last_week)
    categories = set(post.values_list('post_category__name', flat=True))
    subscribers = set(Subscription.objects.filter(category__name__in=categories).values_list('user__email', flat=True))

    subject = f'Новые посты за прошедшую неделю в Ваших любимых тематических категориях!'

    text_content = (

        f'Список новых постов: {post}...\n\n'
        f'Читать: http://127.0.0.1:8000/news/'
    )
    html_content = (
        f'Список новых постов: {post}...<br><br>'
        f'<a href="http://127.0.0.1:8000/news/">'
        f'Скорей ознакомьтесь, если что-то пропустили!</a>')

    msg = EmailMultiAlternatives(subject, text_content, None, subscribers)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    # posts = Post.objects.order_by('-date_creation')
    # text = '\n'.join(['{} - {}'.format(p.date_creation, p.title) for p in posts])
    # mail_managers("Интересные посты за прошлую неделю.", text)


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day_of_week="fri", minute="00", hour="18"),
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
