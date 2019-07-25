from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug_text):
    post = get_object_or_404(Post, slug=slug_text)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context=context)