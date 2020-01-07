import arrow

class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self, id, name, description, url, author, publishedAt, content, urlToImage):
     self.id = id
     self.name = name
     self.description = description
     self.url = url
     self.author = author
     self.content = content
     self.urlToImage = urlToImage
     self.publishedAt = publishedAt
     
     
class Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self, athor, title, description, url, urlToImage, publishedAt):
        self.author =  author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage 
        self.publishedAt = arrow.get(publishedAt).humanize() 
     
    
    
    