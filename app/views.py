from app import app
from flask import render_template,request,url_for,redirect
from .request import get_source,get_article,search_for_article

@app.route('/')
def index():
    articles=get_article()
    sport=search_for_article('sports')
    business=search_for_article('business')
    sources=get_source()
    #Make request to get article from server
    search=request.args.get('search_name')

    if search:
        return redirect(url_for('search',article_name=search))
    else:
        return render_template('index.html',articles=articles,sports=sport,business=business,sources=sources)

    


@app.route('/sports')
def sources():
    sport=search_for_article('sports')
    search=request.args.get('search_name')
    if search:
        return redirect(url_for('search',article_name=search))
    else:
        return render_template('sports.html',sports=sport)


@app.route('/business')
def business():
    business=search_for_article('business')
    search=request.args.get('search_name')
    if search:
        return redirect(url_for('search',article_name=search))
    else:
        return render_template('business.html',business=business)

@app.route('/search/<article_name>')
def search(article_name):
    artcle_name_list=article_name.split(" ")
    artcle_name_format="+".join(artcle_name_list)
    searched_article=search_for_article(artcle_name_format)
    title=f'{article_name}'

    return render_template('search.html',title=title,article=searched_article)
