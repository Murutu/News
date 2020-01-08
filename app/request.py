import requests
import json
from .models import Source #Article
from app.models import Article
# from app import app

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = f'https://newsapi.org/v2/everything?q=all&apiKey=bf2d30bc84e1419abab595739a664dd9'
    
    res = requests.get(sources_url)
    sources_data = res.json().get('articles')
    return process_sources(sources_data)


def process_sources(sources_data):
    '''
    Function that converts source dict into source model
    '''
    sources = []
    for source_data in sources_data:
        source = Source(source_data['source']['id'],source_data['source']['name'], source_data['description'],
                        source_data['url'], source_data['author'], source_data['publishedAt'], source_data['content'], source_data['urlToImage'])
        sources.append(source)
    print(sources)
    return sources

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    articles_url = f'https://newsapi.org/v2/everything?sources={source_id}&apiKey={app.config["NEWS_API_KEY"]}'
    
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
    
