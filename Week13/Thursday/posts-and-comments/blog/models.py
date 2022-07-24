from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')