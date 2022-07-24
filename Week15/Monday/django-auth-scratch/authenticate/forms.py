from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'is_super_duper']