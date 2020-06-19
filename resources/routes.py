#sabhi functions ke routes idhar hain


#importing the functions from the files
from .article import ArticleApi, ArticlesApi


#function call

def initialize_routes(api):
    api.add_resource(ArticlesApi, '/articles')
    api.add_resource(ArticleApi, '/articles/<id>')