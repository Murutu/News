from flask import render_template
from app import create_app
from . import main
from ..request import get_sources, get_articles
# from app import app

@main.route('/')
def index():
    articles = get_sources()
    return render_template("articles.html", articles=articles)

@main.route('/articles/<string:source_id>')
def articles(source_id):
    articles = get_articles(source_id)
    return render_template('articles.html', articles= articles)