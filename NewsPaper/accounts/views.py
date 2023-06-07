from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm, CustomSignupForm


# class SignUp(CreateView):
#     model = User
#     form_class = SignUpForm
#     success_url = '/accounts/login'
#
#     template_name = 'registration/signup.html'



#попытался переопределить вбюшку для кастомизированной формы регистрации с помощью allauth. Не получилось.
# class CustomSignup(CreateView):
#     model = User
#     form_class = CustomSignupForm
#     template_name = 'signup.html'

