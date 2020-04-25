from app import app
from flask import render_template
from .request import get_source,get_article,search_for_article

@app.route('/')
def index():
    articles=get_article()
    sport=search_for_article('sports')
    business=search_for_article('business')
    sources=get_source()
    return render_template('index.html',articles=articles,sports=sport,business=business,sources=sources)



@app.route('/sports')
def sources():
    sport=search_for_article('sports')
    return render_template('sports.html',sports=sport)


