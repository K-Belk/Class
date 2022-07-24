from django.urls import path
from . import views

urlpatterns =  [
    path('posts/', views.all_posts, name='all_posts'),
    path('posts/<int:post_id>', views.id_posts, name='id_post'),
]