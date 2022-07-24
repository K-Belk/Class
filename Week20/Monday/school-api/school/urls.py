from django.urls import path
from . import views

urlpatterns = [
    # student URL's
    path('student/all', views.all_students, name='all_students'),
    path('student/<int:student_id>', views.student_detail, name='student_detail'),
    path('student/new', views.create_student, name='create_student'),
    path('student/<int:student_id>/edit', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete', views.delete_student, name='delete_student'),

    # course URL's
    path('course/all', views.all_courses, name='all_courses'),
    path('course/<int:course_id>', views.course_detail, name='course_detail'),
    path('course/new', views.create_course, name='create_course'),
    path('course/<int:course_id>/edit', views.edit_course, name='edit_course'),
    path('course/<int:course_id>/delete', views.delete_course, name='delete_course'),
]