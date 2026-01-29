from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.PostsListView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),  # primary_key <-> pk
]
