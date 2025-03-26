import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm, UserCreationForm
from django.contrib import messages
from .models import MyForm
from .forms import UserUpdateForm, CustomUserSignupForm
 
# def textResponse(request):
#     if request.method == 'POST' and request.FILES.getlist('myfile'):
#         parsed_text = []
#         api_key = settings.OCR_API_KEY
#         payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

#         for file in request.FILES.getlist('myfile'):
#             response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)
#             results = response.json()
#             for result in results.get("ParsedResults", []):
#                 parsed_text.append(result.get("ParsedText", ""))

#         form = MyForm(initial={'my_textarea': '\n'.join(parsed_text)})
#         return render(request, "result.html", {"form": form})


# def finalResult(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             finalForm = MyForm(initial={'my_textarea': "final_result"})
#             return render(request, "result.html", {"finalForm": finalForm})

# ///////////////////// working
from django import forms
from django.shortcuts import render
import requests
import numpy as np
from django.conf import settings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def textResponse(request):
    """Extract text using OCR.space, apply clustering, and display the result."""
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        parsed_text = []
        api_key = settings.OCR_API_KEY
        payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

        # Extract text from uploaded files
        for file in request.FILES.getlist('myfile'):
            response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)
            results = response.json()
            for result in results.get("ParsedResults", []):
                parsed_text.append(result.get("ParsedText", ""))

        ocr_text = "\n".join(parsed_text)  # Combine extracted text
        clustered_text = cluster_text(ocr_text)  # Apply clustering directly

        return render(request, "result.html", {"clustered_text": clustered_text})  # Pass to template
    
    return redirect("dashboard")


def cluster_text(text):
    """Cluster text using KMeans with TF-IDF vectorization."""
    sentences = [s.strip() for s in text.split("\n") if s.strip()]  # Split into sentences

    if len(sentences) < 2:
        return "Not enough text to cluster."

    # Convert text into TF-IDF feature vectors
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(sentences)

    num_clusters = min(5, len(sentences))  # Limit clusters to max 5
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    clustered_text = '<div id="clustered-text">'  # Wrap everything in a div
    for i in range(num_clusters):
        clustered_text += f'<div class="cluster"><h2>Cluster {i+1}</h2><p>'
        clustered_text += "<br>".join([sentences[j] for j in range(len(sentences)) if labels[j] == i])
        clustered_text += "</p></div>"

    clustered_text += "</div>"

    return clustered_text


# class MyForm(forms.Form):
#     my_textarea = forms.CharField(widget=forms.Textarea, required=False)

# def textResponse(request):
#     """Extract text using OCR.space and display it in a form."""
#     if request.method == 'POST' and request.FILES.getlist('myfile'):
#         parsed_text = []
#         api_key = settings.OCR_API_KEY
#         payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

#         for file in request.FILES.getlist('myfile'):
#             response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)
#             results = response.json()
#             for result in results.get("ParsedResults", []):
#                 parsed_text.append(result.get("ParsedText", ""))

#         ocr_text = "\n".join(parsed_text)  # Combine extracted text
#         form = MyForm(initial={'my_textarea': ocr_text})  # Set initial text

#         return render(request, "result.html", {"form": form})

#     return redirect("dashboard")

# def finalResult(request):
#     """Take user-reviewed text and apply clustering."""
#     if request.method == 'POST':
#         form = MyForm(request.POST)  # Just get the text directly from the form
#         if form.is_valid():
#             user_text = form.cleaned_data['my_textarea']  # No extra processing
#             clustered_text = cluster_text(user_text)  # Apply clustering
            
#             finalForm = MyForm(initial={'my_textarea': clustered_text})  # Update form with clusters
#             return render(request, "result.html", {"finalForm": finalForm})  # Use 'finalform' as expected

# def cluster_text(text):
#     """Cluster text using KMeans with TF-IDF vectorization."""
#     sentences = [s.strip() for s in text.split("\n") if s.strip()]  # Split into sentences

#     if len(sentences) < 2:
#         return "Not enough text to cluster."

#     # Convert text into TF-IDF feature vectors
#     vectorizer = TfidfVectorizer(stop_words="english")
#     X = vectorizer.fit_transform(sentences)

#     num_clusters = min(5, len(sentences))  # Limit clusters
#     kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
#     labels = kmeans.fit_predict(X)

#     clustered_output = ""
#     for i in range(num_clusters):
#         clustered_output += f"Cluster {i+1}:\n"
#         clustered_output += "\n".join([sentences[j] for j in range(len(sentences)) if labels[j] == i])
#         clustered_output += "\n\n"

#     return clustered_output


# # ////////////////////////
# from django import forms
# from django.shortcuts import render
# import requests
# import numpy as np
# from django.conf import settings
# from sklearn.cluster import KMeans
# from sentence_transformers import SentenceTransformer

# # Load BERT Model
# bert_model = SentenceTransformer("all-MiniLM-L6-v2")  # Small and fast BERT model

# class MyForm(forms.Form):
#     my_textarea = forms.CharField(widget=forms.Textarea, required=False)

# def textResponse(request):
#     """Extract text using OCR.space and display it in a form."""
#     if request.method == 'POST' and request.FILES.getlist('myfile'):
#         parsed_text = []
#         api_key = settings.OCR_API_KEY
#         payload = {"apikey": api_key, "OCREngine": 2, "isTable": True}

#         for file in request.FILES.getlist('myfile'):
#             response = requests.post("https://api.ocr.space/parse/image", files={file.name: file}, data=payload)
#             results = response.json()
#             for result in results.get("ParsedResults", []):
#                 parsed_text.append(result.get("ParsedText", ""))

#         ocr_text = "\n".join(parsed_text)  # Combine extracted text
#         form = MyForm(initial={'my_textarea': ocr_text})  # Set initial text

#         return render(request, "result.html", {"form": form})

# def finalResult(request):
#     """Take user-reviewed text and apply BERT-based clustering."""
#     if request.method == 'POST':
#         form = MyForm(request.POST)  # Just get the text directly from the form
#         if form.is_valid():
#             user_text = form.cleaned_data['my_textarea']  # Get user-reviewed text
#             clustered_text = cluster_text(user_text)  # Apply BERT-based clustering
            
#             finalForm = MyForm(initial={'my_textarea': clustered_text})  # Update form with clusters
#             return render(request, "result.html", {"finalForm": finalForm})  # Use 'finalform' as expected

# def cluster_text(text):
#     """Cluster text using BERT embeddings and KMeans."""
#     sentences = [s.strip() for s in text.split("\n") if s.strip()]  # Split into sentences

#     if len(sentences) < 2:
#         return "Not enough text to cluster."

#     # Convert text into BERT embeddings
#     embeddings = bert_model.encode(sentences)

#     num_clusters = min(5, len(sentences))  # Limit clusters
#     kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
#     labels = kmeans.fit_predict(embeddings)

#     clustered_output = ""
#     for i in range(num_clusters):
#         clustered_output += f"Cluster {i+1}:\n"
#         clustered_output += "\n".join([sentences[j] for j in range(len(sentences)) if labels[j] == i])
#         clustered_output += "\n\n"

#     return clustered_output

# ///////////////////////




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
