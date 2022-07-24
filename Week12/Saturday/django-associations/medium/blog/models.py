from django.db import models

class User(models.Model):
    pass


class Post(models.Model):
    # post has one author
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    # comment has one post
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # comment has one author
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
