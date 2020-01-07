from app import app
import requests
import json
from .models import Source #Article
from app.models import Article

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = 'https://newsapi.org/v2/sources?apiKey=apiKey={app.config["NEWS_API_KEY"]}'
    
    res = requests.get(sources_url)
    sources_data = res.json().get('sources')
    # return process_sources(sources_data)


# def process_sources(sources_data):
#     '''
#     Function that converts source dict into source model
#     '''
#     sources = []
#     for source_data in sources_data:
#         source = Source(source_data['id'], source_data['name'], source_data['description'], source_data['url'],
#                          source_data['category'], source_data['langauge'], source_data['country'])
#         sources.append(source)
        
#     return sources 

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    articles_url = 'https://newsapi.org/v2/everything?sources={source_id}&apiKey={app.config["NEWS_API_KEY"]}'
    
    res = requests.get(articles_url)
    articles_data = res.json().get('articles')
    return process_articles(articles_data)

def process_articles(articles_data):
    '''
    Function that converts articles dict into articles model
    '''
    articles = [] 
    for article_data in articles_data:
        article = Article(article_data['author'], article_data['title'], article_data['description'],
                          article_data['url'], article_data['urlToImage'], article_data['publishedAt'])
        articles.append(article)
        return articles  
    
