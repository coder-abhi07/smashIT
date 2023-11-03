from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.index, name="index"),
    path("textResponse", views.textResponse, name="textResponse"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    
    path('result', views.finalResult, name='result'),
    path('about', views.about, name='about'),
]

