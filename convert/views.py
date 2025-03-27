import requests
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django import forms
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from .models import MyForm
from .forms import UserUpdateForm, CustomUserSignupForm



def textResponse(request):
    """Extract text using OCR.space, apply clustering, and display the result."""
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        parsed_text = []
        api_key = settings.OCR_API_KEY
        payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

        for file in request.FILES.getlist('myfile'):
            response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)

            if response.status_code != 200:
                return custom_error_view(request)  # Render 500 error page

            results = response.json()

            if results.get("IsErroredOnProcessing", False):
                error_message = results.get("ErrorMessage", ["Unknown error"])[0]
                return custom_error_view(request)  # Show custom 500 error page

            for result in results.get("ParsedResults", []):
                parsed_text.append(result.get("ParsedText", "").strip())

        ocr_text = "\n".join(parsed_text).strip()

        if not ocr_text:
            return custom_error_view(request)  # Show 500 error if no text extracted

        clustered_text = cluster_text(ocr_text)

        return render(request, "result.html", {"clustered_text": clustered_text})

    return custom_bad_request_view(request)  # Show 400 error if invalid request


def cluster_text(text):
    """Cluster text using KMeans with TF-IDF vectorization."""
    sentences = [s.strip() for s in text.split("\n") if s.strip()]

    if len(sentences) < 2:
        return "Not enough text to cluster."

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(sentences)

    num_clusters = min(5, len(sentences))
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    clustered_text = '<div id="clustered-text">'
    for i in range(num_clusters):
        clustered_text += f'<div class="cluster"><h2>Cluster {i+1}</h2><p>'
        clustered_text += "<br>".join([sentences[j] for j in range(len(sentences)) if labels[j] == i])
        clustered_text += "</p></div>"

    clustered_text += "</div>"

    return clustered_text


def custom_page_not_found_view(request, exception = None):
    return render(request, "404.html")


def custom_error_view(request, exception=None):
    return render(request, "500.html")


def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html")


def custom_bad_request_view(request, exception=None):
    return render(request, "400.html")


def about(request):
    return render(request, "about.html")


def index(request):
    return render(request, "index.html")


@login_required
def change_password(request):
    if request.user.has_usable_password():
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in
                messages.success(request, 'Your password has been successfully updated!')
                return redirect('user_profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)

        return render(request, 'change_password.html', {'form': form})

    return redirect('set_password')


@login_required
def set_password(request):
    if not request.user.has_usable_password():
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Keeps the user logged in
                messages.success(request, 'Your password has been successfully set!')
                return redirect('user_profile')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = SetPasswordForm(request.user)

        return render(request, 'set_password.html', {'form': form})

    return redirect('change_password')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserSignupForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    if (request.method == "POST"):
        return redirect ("textResponse")

    return render(request, "dashboard.html")
    
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('user_profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'update_profile.html', {'form': form})








# def textResponse(request):
#     """Extract text using OCR.space, apply clustering, and display the result."""
#     if request.method == 'POST' and request.FILES.getlist('myfile'):
#         parsed_text = []
#         api_key = settings.OCR_API_KEY
#         gemini_key = settings.GEMINI_API_KEY  # Store API key in settings.py
#         payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

#         for file in request.FILES.getlist('myfile'):
#             response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)

#             if response.status_code != 200:
#                 return custom_error_view(request)  # Render 500 error page

#             results = response.json()

#             if results.get("IsErroredOnProcessing", False):
#                 return custom_error_view(request)  # Show custom 500 error page

#             for result in results.get("ParsedResults", []):
#                 parsed_text.append(result.get("ParsedText", "").strip())

#         ocr_text = "\n".join(parsed_text).strip()

#         if not ocr_text:
#             return custom_error_view(request)  # Show 500 error if no text extracted

#         # Use Gemini API for better clustering
#         clustered_text = cluster_with_gemini(ocr_text, gemini_key)

#         return render(request, "result.html", {"clustered_text": clustered_text})

#     return custom_bad_request_view(request)  # Show 400 error if invalid request

# def cluster_with_gemini(text, api_key):
#     """Send extracted text to Gemini API using requests and get clustered questions."""
#     if not text.strip():
#         return "No text available for clustering."

#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
#     headers = {"Content-Type": "application/json"}
#     params = {"key": api_key}
#     data = {
#         "contents": [{"parts": [{"text": f"Cluster the following questions into relevant categories:\n\n{text}\n\nGroup them under appropriate topics."}]}]
#     }

#     try:
#         response = requests.post(url, headers=headers, params=params, json=data)
#         response.raise_for_status()  # Raise an error for bad responses
#         result = response.json()

#         # Extract response text
#         raw_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No clustering result.")

#         # Convert response to HTML format
#         clustered_text = '<div id="clustered-text">'
#         clusters = raw_text.split("\n\n")  # Assume Gemini returns clusters separated by two newlines

#         for i, cluster in enumerate(clusters):
#             lines = cluster.split("\n")
#             if lines:
#                 clustered_text += f'<div class="cluster"><h2>Cluster {i+1}</h2><p>'
#                 clustered_text += "<br>".join(lines)
#                 clustered_text += "</p></div>"

#         clustered_text += "</div>"

#         return clustered_text
#     except requests.exceptions.RequestException as e:
#         return f"<div>Error processing with Gemini: {str(e)}</div>"