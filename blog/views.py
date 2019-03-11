from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'blog/home.html')


def posts(request):
    context = {
        'title': 'posts',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/posts.html', context)


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'title': 'post' + post.title,
        'post': get_object_or_404(Post, pk=pk),
    }
    return render(request, 'blog/post.html', context)
