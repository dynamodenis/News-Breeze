from app import app
from flask import render_template
from .request import get_source,get_article,search_for_article

@app.route('/')
def index():
    articles=get_article()
    sport=search_for_article('sports')
    business=search_for_article('business')
    return render_template('index.html',articles=articles,sports=sport,business=business)



@app.route('/sources')
def sources():
    sources=get_source()
    return render_template('source.html',source=sources)


