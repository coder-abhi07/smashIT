from django.db import models
from django import forms

class MyForm(forms.Form):
    my_textarea = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'my_textarea'}),label="text response")

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
