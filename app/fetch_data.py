from app import app
import requests
import json
from .models import Source, Article

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = 'https://newsapi.org/v2/sources?apiKey=apiKey={app.config["NEWS_API_KEY"]}'
    
    res = requests.get(sources_url)
    sources_data
    
