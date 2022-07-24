from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self) -> str:
        return f"ID: {self.id} Title: {self.title}"