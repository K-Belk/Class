from django.db import models

class Comments(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateField(auto_now=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='comments', blank=True)

    def __str__(self) -> str:
        return self.title