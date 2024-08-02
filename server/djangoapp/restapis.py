import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

# Load URLs from environment variables
backend_url = os.getenv('BACKEND_URL', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('SENTIMENT_ANALYZER_URL', default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = "&".join(f"{key}={value}" for key, value in kwargs.items())
    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")

def analyze_review_sentiments(text):
    encoded_text = quote(text)
    request_url = f"{sentiment_analyzer_url}/analyze/{encoded_text}"
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error occurred: {e}")
        return None

def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    print(f"POST to {request_url} with data {data_dict}")
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
