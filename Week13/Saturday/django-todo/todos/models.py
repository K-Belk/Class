from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=255)