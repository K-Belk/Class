from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comments
from .serializer import PostSerializer, CommentsSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer



