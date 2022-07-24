from django.db import models

class Bloggin(models.Model):
    title = models.CharField(max_length=250)
    post = models.TextField()