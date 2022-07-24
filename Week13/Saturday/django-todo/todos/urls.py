from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('new/', views.todo_new, name='todo_new'),
    path('<int:todo_id>', views.todo_show, name='todo_show'),
    path('<int:todo_id>/edit/', views.todo_update, name='todo_update'),
    path('<int:todo_id>/delete/', views.todo_delete, name='todo_delete'),
    
]