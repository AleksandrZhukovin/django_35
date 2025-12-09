from django.shortcuts import render

from .forms import PostForm
from .models import Post


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # post = Post(content=form.cleaned_data['content'], user=request.user)
            # post.save()
            Post.objects.create(content=form.cleaned_data['content'], user=request.user)
    return render(request, 'blog/posts/create_post.html', {"form": form})
