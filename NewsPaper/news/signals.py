# from django.db.models.signals import post_save, m2m_changed
# from django.dispatch import receiver
#
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from .models import Post, PostCategory
# from subscriptions.models import Subscription
# from django.template.loader import render_to_string
#
# #========здесь реализация какого-то человека, реализовал по своему
# def send_notifications(text, pk, title, subscribers_emails, categories):
#     # здсь описана работа рендера прикрепления тэмплейт шаблонов для писем
#     html_content = render_to_string(
#         'email/post_created_email.html',
#         {
#             'title' : title,
#             'text' : text,
#             'categ' : [cat.name for cat in categories],
#             'link' : f'http://127.0.0.1:8000/news/{pk}',
#             'user' : User.username
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
#
#
#
#
#
# #=======А НИЖЕ РЕАЛИЗАЦИЯ СИГНАЛА ДЛЯ УЧЕБНОГО ПРОЕКТА С РАЗДЕЛА. НО ОН НЕ РАБОТАЕТ ЧТО-ТО, Т.К. ЕСТЬ СВЯЗЬ Many2Many
# # @receiver(post_save, sender=Post)
# # def post_created(instance, created, **kwargs):
# #     print('Новый пост!', instance.post_category.all())  #чисто тест для вывода сигнала в консоль
#     # if not created:
#     #     return
#     #
#     # emails = User.objects.filter(
#     #     subscriptions__category=instance.post_category
#     # ).values_list('email', flat=True)
#     #
#     # subject = f'Новый пост в тематической категории "{instance.post_category}"!\n'
#     #
#     # text_content = (
#     #     f'Тема повестки: {instance.title}\n'
#     #     f'Превью: {instance.text[:20]}\n\n'
#     #     f'Узнайте первыми: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     # )
#     # html_content = (
#     #     f'Повестка дня: {instance.title}<br>'
#     #     f'Превью: {instance.text[:20]}<br><br>'
#     #     f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#     #     f'Узнайте первыми!</a>'
#     # )
#     # for email in emails:
#     #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
#     #     msg.attach_alternative(html_content, "text/html")
#     #     msg.send()
#
