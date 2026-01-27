from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .forms import PostForm
from .models import Post


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(content=form.cleaned_data['content'], user=request.user)
    return render(request, 'blog/posts/create_post.html', {"form": form})


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/posts/create_post.html'
    form_class = PostForm
    success_url = '/home'


# def home(request):
#     posts = Post.objects.all().prefetch_related('comments').select_related('user')  # QuerySet [1, 2, 3, 4, ....]
#     #  Post.objects.filter(user=request.user, content="Hello")
#     #  Post.objects.get(content="Hello")  object, instance   <- Get must return 1 instance, returned multiple instead
#     #  Post.objects.get(id=2)
#     return render(request, "blog/home.html", {"posts": posts})


class PostsListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
