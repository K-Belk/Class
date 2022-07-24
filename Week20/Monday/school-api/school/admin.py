from django.contrib import admin
from .models import Students, Courses

admin.site.register(Courses)
admin.site.register(Students)