from django.shortcuts import render
from .models import Post, Comment

def get_post(post_id):
    return Post.objects.get(id=post_id)

def all_posts(request):
    the_posts = Post.objects.order_by('id')
    return render(request, 'blog/all.html', {'all_post': the_posts})

def id_posts(request, post_id):
    post = get_post(post_id)
    comments = post.comment.all()
    data = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/post.html', data)