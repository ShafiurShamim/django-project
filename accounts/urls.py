from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]
