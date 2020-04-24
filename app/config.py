class Config:
    HEADLINES_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True