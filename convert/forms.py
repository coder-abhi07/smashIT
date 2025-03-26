from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',  'avatar_url']


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserSignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "name@example.com"})
    )
    avatar_url = forms.URLField(
    required=False,  # Optional field
    widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "https://example.com/avatar.jpg"})
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "avatar_url"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "John Doe"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "••••••••"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "••••••••"}),
        }
