from app import app
from flask import render_template
from .request import get_source

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/sources')
def sources():
    sources=get_source()
    return render_template('source.html',source=sources)


