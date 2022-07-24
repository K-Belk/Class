from django.urls import path
from . import views

urlpatterns = [
    path('', views.cohort_list, name='cohort_list'), # list all the cohorts
    path('new', views.new_cohort, name='new_cohort'), # form page for creating a new cohort
    path('<int:cohort_id>', views.cohort_detail, name='cohort_detail'), # view details about an existing cohort
    path('<int:cohort_id>/edit', views.edit_cohort, name='edit_cohort'), # form page for editing a cohort
    path('<int:cohort_id>/delete', views.delete_cohort, name='delete_cohort'), # delete a cohort
    path('<int:cohort_id>/students', views.student_list, name='student_list'), # list all of the students for a cohort
    path('<int:cohort_id>/students/new', views.new_student, name='new_student'), # form page for creating a new student for a cohort
    path('<int:cohort_id>/students/<int:student_id>', views.student_detail, name='student_detail'), # view details about a student in a cohort
    path('<int:cohort_id>/students/<int:student_id>/edit', views.edit_student, name='edit_student'), # form page for editing a student for a cohort
    path('<int:cohort_id>/students/<int:student_id>/delete', views.delete_student, name='delete_student'), # delete a student for a cohort
]