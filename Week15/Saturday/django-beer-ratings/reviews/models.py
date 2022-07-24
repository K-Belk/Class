from django.db import models
from django.conf import settings

class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.CharField(max_length=255)

class Reviews(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()