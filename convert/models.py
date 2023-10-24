from django.db import models
from django import forms

class MyForm(forms.Form):
    my_textarea = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'my_textarea'}),label="text response")
