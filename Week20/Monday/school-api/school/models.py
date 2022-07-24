from django.db import models


class Students(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    enrolled_students = models.ManyToManyField(Students)

    def __str__(self) -> str:
        return self.course_name