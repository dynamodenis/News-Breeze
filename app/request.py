from app import app
import urllib.request,json
from .models import Source,Article


#import API key
api_key=app.config['API_KEY']

#import urls
highlights_url=app.config['HEADLINES_API_URL']
sources_url=app.config['SOURCE_API_URL']

def get_source():
    source_api_url=sources_url.format(api_key)

    with urllib.request.urlopen(source_api_url) as url:
        unread_data=url.read()
        read_json=json.loads(unread_data)

        source_results=None

        if read_json['sources']:
            sources_list=read_json['sources']
            source_results=process_results(sources_list)

    return source_results


def process_results(source_list):
    source_results=[]

    for sources in source_list:
        id=sources.get('id')
        name=sources.get('name')
        description=sources.get('description')
        url=sources.get('url')
        

        new_source=Source(id,name,description,url)
        source_results.append(new_source)

    return source_results


def get_article():
    get_highlights_url=highlights_url.format(api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_data=url.read()
        get_json_data=json.loads(get_data)

        articles_data=None

        if get_json_data['articles']:
            articles_list=get_json_data['articles']
            articles_data=process_article(articles_list)
        
    return articles_data

def process_article(articles_list):
    articles_data=[]

    for article in articles_list:
        id=article.get('id')
        name=article.get('name')
        urlToImage=article.get('urlToImage')
        description=article.get('description')
        publishedAt=article.get('publishedAt')
        url=article.get('url')
        title=article.get('title')
        source=article.get('source')
        
        new_article=Article(id,name,urlToImage,description,title,url,publishedAt,source)
        articles_data.append(new_article)

    return articles_data




