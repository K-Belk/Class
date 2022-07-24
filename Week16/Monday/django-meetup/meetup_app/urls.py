from django.urls import path
from . import views

app_name = 'meet'

urlpatterns = [
#   -----Groups-----
    path('groups/', views.all_groups, name='all_groups'),
    path('new_group/', views.AddGroupView.as_view(), name='add_group'),
    path('<int:group_id>/', views.GroupDetailView.as_view(), name='group_details'),
    path('<pk>/update/', views.GroupUpdateView.as_view(), name='update_group'),
    path('<pk>/delete/', views.GroupDeleteView.as_view(), name='delete_group'),

#   -----Events-----
    path('<int:group_id>/add_event/', views.AddEventView.as_view(), name='add_event'),
    path('<int:group_id>/<int:event_id>/edit_event', views.EditEventView.as_view(), name='edit_event'),
    path('<int:group_id>/<int:event_id>/delete_event', views.DeleteEventView.as_view(), name='delete_event'),
]
