from flask_mongoengine import MongoEngine

db = MongoEngine()          #object db

def initialize_db(app):
    db.init_app(app)

