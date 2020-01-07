from flask import render_template
from app import app
from .fetch_data import get_sources, get_articles

@app.route('/')
def index():
    sources = get_sources()
    return render_template("index.html", sources=sources)

@app.route('/articles/<string:source_id>')
def articles(source_id):
    articles = get_articles(source_id)
    return render_template('articles.html', articles= articles)