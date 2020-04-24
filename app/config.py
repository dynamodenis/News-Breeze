class Config:
    API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True