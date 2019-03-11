from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('posts/', views.posts, name='blog-posts'),
    path('post/<int:pk>/', views.post, name='blog-post'),
]
