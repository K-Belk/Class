from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=30)

class Posts(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    description = models.TextField()
