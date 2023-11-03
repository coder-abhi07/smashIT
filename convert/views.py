import pandas as pd
import numpy as np
import logging
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster
from .models import MyForm
from django.conf import settings
import requests
from nltk.stem import PorterStemmer


from authlib.integrations.django_client import OAuth

from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode


# import hdbscan
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import json

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

def textResponse(request):
    if request.method == 'POST' and request.FILES.getlist('myfile'):
        
        parsed_text = ""
        api_key = settings.OCR_API_KEY
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

def finalResult(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the text from the form (file or textarea)
            questions_text = form.cleaned_data['my_textarea']

            # Tokenize the input questions
            questions = questions_text.split("\n")  # Assuming questions are separated by newlines

            tfidf = TfidfVectorizer(tokenizer=tokenizer, stop_words=sw)
            X = pd.DataFrame(tfidf.fit_transform(questions).toarray(),
                 index=questions, columns=tfidf.get_feature_names_out())
            c = cluster.AffinityPropagation()
            pred = c.fit_predict(X)

            c.fit_predict(X)
            X['pred'] = c.fit_predict(X)
           # Original unprocessed questions
            df = pd.DataFrame(X['pred'])

            
            X['pred'] = c.fit_predict(X)

            predicted_clusters = X['pred'].tolist()
            # Create a mapping between cluster labels and the original strings
            cluster_mapping = {}

            for cluster_label, original_string in zip(predicted_clusters, questions):
                if cluster_label not in cluster_mapping:
                    cluster_mapping[cluster_label] = [original_string]
                else:
                    cluster_mapping[cluster_label].append(original_string)

            finalResultString =  ""
            # Print the original strings for each cluster
            for cluster_label, original_strings in cluster_mapping.items():
                
                for string in original_strings:
                    finalResultString += string
                finalResultString += '\n'

        
            finalForm = MyForm()
            finalForm.fields['my_textarea'].initial = finalResultString
            

            return render(request, "result.html", {"finalForm": finalForm})

# Create a logger with a specific name for your view function
logger = logging.getLogger('convert.views')


def custom_page_not_found_view(request, exception):
    logger.error('Page Not Found: %s', request.path)
    error_message = "The page you are looking for does not exist."
    return render(request, "404.html", {'error_message': error_message}, status=404)

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "400.html", {})



def about(request):
    return render(request, "about.html")

