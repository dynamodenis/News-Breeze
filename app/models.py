class Source:
    def __init__(self,id,name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url


class Article:
    def __init__(self,id,name,urlToImage,description,title,url):
        self.id=id
        self.name=name
        self.urlToImage=urlToImage
        self.description=description
        self.title=title
        self.url=url