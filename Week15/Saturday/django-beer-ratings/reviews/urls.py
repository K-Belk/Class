from django.urls import path
from . import views

app_name = 'beer'

urlpatterns = [
    path('', views.beer_list, name='beer_list'),
    path('new/', views.new_beer, name='new_beer'),
    path('<int:beer_id>/', views.beer_details, name='beer_details'),
    path('<int:beer_id>/update/', views.update_beer, name='update_beer'),
    path('<int:beer_id>/delete/', views.delete_beer, name='delete_beer'),

    path('<int:beer_id>/<int:user_id>/review/', views.add_review, name='add_review'),
    path('<int:review_id>/update_review', views.update_review, name='update_review'),
    path('<int:review_id>/delete_review', views.delete_review, name='delete_review'),

]
    