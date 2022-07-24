from django.db import models

class Wine(models.Model):
    wine_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    varietal = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.wine_name