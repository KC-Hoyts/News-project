# #from celery import shared_task
# import datetime
# from news.models import Post
# from subscriptions.models import Subscription
# from django.core.mail import EmailMultiAlternatives
#
# from django.db.models.signals import post_save, m2m_changed
#
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from .models import Post, PostCategory
# from subscriptions.models import Subscription
# from django.template.loader import render_to_string
#
# from django.db.models.signals import post_save, m2m_changed
# from django.dispatch import receiver
#
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from .models import Post, PostCategory
# from subscriptions.models import Subscription
# from django.template.loader import render_to_string
#
#
# #Здесь уже подробный код каждой задачи по расписанию
# @shared_task
# def week_mailing():
#     today = datetime.datetime.now()
#     last_week = today - datetime.timedelta(days=7)
#     post = Post.objects.filter(date_creation__gte=last_week)
#     categories = set(post.values_list('post_category__name', flat=True))
#     subscribers = set(Subscription.objects.filter(category__name__in=categories).values_list('user__email', flat=True))
#
#     posts_list = []
#     for i in post.values("title"):
#         posts_list.append(("<br>"))
#         posts_list.append(i['title'])
#
#
#
#     subject = f'Новые посты за прошедшую неделю в Ваших любимых тематических категориях!'
#
#     text_content = (
#
#         f'Список новых постов здеся: {post.values("title")}...\n\n'
#         f'Читать: http://127.0.0.1:8000/news/'
#     )
#     html_content = (
#         f'Список новых постов тут: {posts_list}...<br><br>'
#         f'<a href="http://127.0.0.1:8000/news/">'
#         f'Скорей ознакомьтесь, если что-то пропустили!</a>')
#
#     msg = EmailMultiAlternatives(subject, text_content, None, subscribers)
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#
# #------------
# @shared_task
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.post_category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = Subscription.objects.filter(category=cat)
#             subscribers_emails += [subs.user.email for subs in subscribers]
#
#         send_notifications(instance.text[:30], instance.pk, instance.title, subscribers_emails, categories)
#
# def send_notifications(text, pk, title, subscribers_emails, categories):
#     # здсь описана работа рендера прикрепления тэмплейт шаблонов для писем
#     html_content = render_to_string(
#         'email/post_created_email.html',
#         {
#             'title' : title,
#             'text' : text,
#             'categ' : [cat.name for cat in categories],
#             'link' : f'http://127.0.0.1:8000/news/{pk}',
#
#         }
#     )
#     subject = f'Новый пост в Вашей любимой тематической категории!'
#
#     text_content = (
#         f'Тема повестки: {title}\n'
#         f'Превью: {text}...\n\n'
#         f'Узнайте первыми: http://127.0.0.1:8000/news/{pk}'
#     )
#     # html_content = (
#     #     f'Повестка дня: {title}<br>'
#     #     f'Превью: {text}...<br><br>'
#     #     f'<a href="http://127.0.0.1:8000/news/{pk}">'
#     #     f'Узнайте первыми!</a>')
#
#     msg = EmailMultiAlternatives(subject, text_content, None, subscribers_emails)
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#
#
#

