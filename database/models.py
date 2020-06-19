from .db import db 

class Article(db.Document):
    name = db.StringField(required=True, unique=True)
    desc = db.ListField(db.StringField())
    #desc = db.StringField(max_length=200, required=True)
    domains = db.ListField(db.StringField())
    link = db.StringField()