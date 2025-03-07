from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("", views.index, name="index"),
    path("textResponse", views.textResponse, name="textResponse"),
    

    path('password/change/', views.change_password, name='password_change'),
    path('password/set/', views.set_password, name='set_password'),
    path('login/', views.user_login, name='login'),

    path('signup/', views.signup_view, name='signup'),
    path("logout/", views.user_logout, name="logout"), 
    path('profile/', views.user_profile, name='user_profile'),  # User profile
    path('profile/update/', views.update_profile, name='update_profile'),  # Update profile


    path('accounts/', include('allauth.urls')),  # Google OAuth routes
    
    path('result', views.finalResult, name='result'),
    path('about', views.about, name='about'),
]

