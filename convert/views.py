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
    

    # if request.method == 'POST':
    #     form = MyForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         text = form.cleaned_data['my_textarea']
    #         return render(request, "result.html", {'questions': text})
        
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

def finalResult(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the text from the form (file or textarea)
            questions_text = form.cleaned_data['my_textarea']

            # Tokenize the input questions
            questions = questions_text.split("\n")  # Assuming questions are separated by newlines

            # Perform stemming and lemmatization on the words
            stemmer = PorterStemmer()
            sw = stopwords.words('english')

            def preprocess_question(question):
                words = [stemmer.stem(word) for word in question.split() if word not in sw]
                return " ".join(words)

            processed_questions = [preprocess_question(question) for question in questions]

            # Vectorize the processed questions (using CountVectorizer)
            vectorizer = CountVectorizer()
            X = vectorizer.fit_transform(processed_questions)
            X = X.toarray()

            # Apply K-Means clustering on processed questions
            num_clusters = 3  # You can adjust the number of clusters as needed
            kmeans = KMeans(n_clusters=num_clusters, random_state=0)
            labels = kmeans.fit_predict(X)

            # Create a list to store cluster assignments
            clusters = labels.tolist()

            # Convert processed questions to a string
            processed_questions_text = "\n".join(processed_questions)
           # Original unprocessed questions

            finalForm = MyForm()
            finalForm.fields['my_textarea'].initial = processed_questions_text  # Display the original questions

            return render(request, "result.html", 
                          context={"session": request.session.get("user"),
                                   "pretty": json.dumps(request.session.get("user"), indent=4),
                                   "finalForm": finalForm,
                               })
