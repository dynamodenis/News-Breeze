from app import app
from flask import render_template
from .request import get_source,get_article

@app.route('/')
def index():
    articles=get_article()
    return render_template('index.html',articles=articles)



@app.route('/sources')
def sources():
    sources=get_source()
    return render_template('source.html',source=sources)


