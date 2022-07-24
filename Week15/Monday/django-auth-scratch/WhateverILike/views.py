from django.shortcuts import render
from .models import Bloggin

def all_post(request):
    posts = Bloggin.objects.all()
    return render(request, 'WhateverILike/all-post.html', {'posts': posts})