class Config:
    HEADLINES_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'
    SEARCH_SOURCES='https://newsapi.org/v2/everything?q={}&apiKey={}'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True