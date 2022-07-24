from .forms import UserSignupForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

class UserSignup(CreateView):
    model = get_user_model()
    form_class = UserSignupForm
    template_name = 'user_auth/signup.html'
    success_url = '/auth/'

class CustomLogoutView(LogoutView):
    next_page = '/auth/'