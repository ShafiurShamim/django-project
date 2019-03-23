from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.models import Post
from blog.forms import PostCreateForm, PostUpdateForm


def post_list_view(request):
    context = {
        'posts': Post.objects.all().order_by('-date_created'),
    }
    return render(request, 'blog/home.html', context)


def post_detail_view(request, pk):
    context = {
        'post': get_object_or_404(Post, pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
def post_create_view(request):
    if request.method == 'POST':
        post_form = PostCreateForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            messages.success(
                request, f'Your post has been created!')
            return redirect(post.get_absolute_url())
    else:
        post_form = PostCreateForm()
    return render(request, 'blog/post_form.html', {'form': post_form})


@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk, author_id=request.user.id)
    if request.method == 'POST':
        if request.FILES:
            post.image.delete()
        update_form = PostUpdateForm(
            request.POST, request.FILES, instance=post)
        if update_form.is_valid():
            form = update_form.save(commit=False)
            form.author_id = request.user.id
            form.save()
            messages.success(
                request, f'Your post has been Updated!')
            return redirect(post.get_absolute_url())
    else:
        update_form = PostUpdateForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': update_form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk, author_id=request.user.id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Your Post has been deleted!')
        return redirect('blog-home')
    else:
        return render(request, 'blog/post_confirm_delete.html', {'post': post})
