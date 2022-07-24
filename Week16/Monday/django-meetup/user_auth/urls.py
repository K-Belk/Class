from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'auth'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name='login_user'),
    path('signup/', views.UserSignup.as_view(), name='user_signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='user_logout')
]