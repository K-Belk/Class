from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('next_shows', views.next_shows, name='next_shows'),

]