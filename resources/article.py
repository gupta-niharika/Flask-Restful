# Article ke functions idhar hai!

from flask import Response, request
from database.models import Article
from flask_restful import Resource

#sare routes ko class and functions me badal diye hain

class ArticlesApi(Resource):
    def get(self):                      #view all articles - R
        articles = Article.objects().to_json()
        return Response(articles, mimetype="application/json", status=200)         #prints whatever is present in that colection

    def post(self):             #create an article - C
        body = request.get_json()
        article = Article(**body).save()                   #collection = Class(**body).save() <-- syntax samajh lo
        id = article.id
        return 'article add ho gayi', 200

class ArticleApi(Resource):    #separately banaye coz isme id padegi url me hi
    def delete(self, id):               #delete an article - D
        article = Article.objects.get(id=id).delete()
        return 'article delete ho gayi', 200