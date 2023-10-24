from django.shortcuts import render
from .models import MyForm

from django.conf import settings
import requests
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster
import nltk


import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AffinityPropagation

# import hdbscan
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Download NLTK stopwords data
nltk.download('stopwords')


stemmer = PorterStemmer()
sw = stopwords.words('english')

def tokenizer(keyword):
    return [stemmer.stem(w) for w in keyword.split()]

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def index(request):

    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['my_textarea']
            return render(request, "result.html", {'questions': text})
        
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        
        parsed_text = ""
        api_key = "K86627853288957" 
        payload = {
        'apikey': api_key,
        'OCREngine': 3,
        'isTable': True
        }

        for file in request.FILES.getlist('myfile'):
            response = requests.post('https://api.ocr.space/parse/image',
                                     files={file.name: file},
                                     data=payload)
            results = response.json()
            for result in results['ParsedResults']:
                parsed_text += result['ParsedText']


        
       
        form = MyForm()
        form.fields['my_textarea'].initial = parsed_text
        
        return render(request, 'result.html', {'form': form})
    
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def result11(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the text from the form (file or textarea)
            questions_text = form.cleaned_data['my_textarea']
            # Tokenize the input questions
            questions = questions_text.split("\n")  # Assuming questions are separated by newlines
            
            # Vectorize the questions (you may use more advanced techniques here)
            # For this example, we're using simple Bag of Words (BoW) vectorization.
            vectorizer = CountVectorizer()
            X = vectorizer.fit_transform(questions)
            X = X.toarray()

            # Apply HDBSCAN clustering
            clusterer = hdbscan.HDBSCAN(min_cluster_size=3)
            labels = clusterer.fit_predict(X)

            # Organize questions into clusters
            clusters = {}
            for label, question in zip(labels, questions):
                if label in clusters:
                    clusters[label].append(question)
                else:
                    clusters[label] = [question]

            return render(request, "result.html", {'questions': questions, 'clusters': clusters})