from django.shortcuts import render
from .forms import UserSignupForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LogoutView


class UserSignup(CreateView):
    model = AbstractUser
    form_class = UserSignupForm
    template_name = 'user_auth/signup.html'
    success_url = '/auth/'

class CustomLogoutView(LogoutView):
    next_page = '/auth/'
