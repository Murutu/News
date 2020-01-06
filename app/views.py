from flask import render_template
from app import app
from .fetch_data import get_sources, get_articles

@app.route('/')
def index():
    sources = get_sources()
    return render