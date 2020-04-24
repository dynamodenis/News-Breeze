from app import app
import urllib.request,json
from .models import Source


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

