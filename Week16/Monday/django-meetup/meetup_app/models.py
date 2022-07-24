from django.db import models
from django.contrib.auth import get_user_model

class Group(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(get_user_model())
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events')
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image_url = models.URLField(null=True)

    def __str__(self) -> str:
        return self.title