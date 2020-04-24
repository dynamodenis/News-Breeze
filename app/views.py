from app import app
from flask import render_template
from .request import get_source


@app.route('/')
def hello():
    sources=get_source()
    return render_template('index.html',source=sources)


