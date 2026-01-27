from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.PostsListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
]
