from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_signup_redirect_url(self, request):
        return "/" 

    def pre_social_login(self, request, sociallogin):
    
        email = sociallogin.account.extra_data.get("email")
        User = get_user_model()

        if not email:
            return  # No email, can't match

        try:
            existing_user = User.objects.get(email=email)

            # Link the social account to the existing Django user
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            pass  # No existing user, normal signup/login will proceed