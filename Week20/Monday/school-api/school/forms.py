from dataclasses import field
from django import forms
from .models import Students, Courses

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name']

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name', 'enrolled_students']