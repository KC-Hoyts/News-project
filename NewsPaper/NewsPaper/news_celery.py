import os
# from celery import Celery
# from celery.schedules import crontab
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
#
# app = Celery('NewsPaper')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# #
# # app.conf.enable_utc = False
# # app.conf.timezone = "Asia/Calcutta" #change to your timezone
#
# app.autodiscover_tasks()
#
# #добавление задач по расписанию
# app.conf.beat_schedule = {
#     'weekly_newsletter': {
#         'task': 'news.tasks.week_mailing',
#         'schedule': crontab(hour=19, minute=34, day_of_week=3),
#     },
# }