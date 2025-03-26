from django.urls import path, include
from . import views
from allauth.socialaccount.views import LoginCancelledView
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = [
    
    path("", views.index, name="index"),
    path("result", views.textResponse, name="textResponse"),
    # path("400", views.custom_bad_request_view, name="400"),
    # path("403", views.custom_permission_denied_view, name="403"),
    # path("404", views.custom_page_not_found_view, name="404"),
    # path("500", views.custom_error_view, name="500"),

    

    path('password/change/', views.change_password, name='password_change'),
    path('password/set/', views.set_password, name='set_password'),
    path('login/', views.user_login, name='login'),

    path('signup/', views.signup_view, name='signup'),
    path("logout/", views.user_logout, name="logout"), 
    path('profile/', views.user_profile, name='user_profile'),  # User profile
    path('profile/update/', views.update_profile, name='update_profile'),  # Update profile


    path('accounts/', include('allauth.urls')),  # Google OAuth routes

    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

