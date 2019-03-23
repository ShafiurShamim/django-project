from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list_view, name='blog-home'),
    path('post/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('post/create/', views.post_create_view, name='post-create'),
    path('post/<int:pk>/update/', views.post_update_view, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete_view, name='post-delete'),
]
