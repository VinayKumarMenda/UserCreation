from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('',All_Users,name='Home_Page'),
    path('register',Register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('profile',Profile,name='profile'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
]  
