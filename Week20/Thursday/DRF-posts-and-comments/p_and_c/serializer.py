from rest_framework import serializers
from .models import Post, Comments


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'pub_date', 'comments']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'title', 'body', 'pub_date']
