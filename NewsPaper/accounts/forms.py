from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django.core.mail import send_mail, EmailMultiAlternatives, mail_managers, mail_admins


#для регистрации при кодключенном auth
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

#для регистрации через allauth с автодобавлением нового юзера в группу
class CustomSignupForm(SignupForm):


    def save(self, request):
        user = super().save(request)
        subscribers = Group.objects.get(name="Subscribers")
        user.groups.add(subscribers)

# ФУНКЦИЮ RENDER_TO_STRING СМОТРИ В SIGNALS.PY (ТАМ ЕСТЬ РАБОТАЮЩИЙ ПРИМЕР)

# простой сэмпл письма в текстовом варианте
        # send_mail(
        #     subject='Добро пожаловать в наш интернет-магазин!',
        #     message=f'{user.username}, вы успешно зарегистрировались!',
        #     from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
        #     recipient_list=[user.email],
        # )

#отправка письма с поддержкой html кода
        subject = 'Добро пожаловать на наш новостной портал!'
        text = f'{user.username}, вы успешно зарегистрировались на портале!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/news">портале</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

# ----------------------------------
    # уведомление менеджеров о подключении нового пользователя
        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} / {user.email} зарегистрировался на сайте.'
        )

    # то же но для админов
        # mail_admins(
        #     subject='Новый пользователь!',
        #     message=f'Пользователь {user.username} / {user.email} зарегистрировался на сайте.'
        # )

        return user



