# Dependencies
# pip install flask
# pip install flask-mongoengine (latest)
# pip install flask-restful

from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

#atlas connected with IP 0.0.0.0 /  dont touch this, its working!
#python driver version = 3.4+       <-- coz srv not supported -_-
app.config['MONGODB_HOST'] = 'mongodb://admin:admin@cluster0-shard-00-00-iim6b.mongodb.net:27017,cluster0-shard-00-01-iim6b.mongodb.net:27017,cluster0-shard-00-02-iim6b.mongodb.net:27017/MSTC?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'
app.config['MONGODB_DB'] = 'MSTC'
initialize_db(app)
# dont touch till here

initialize_routes(api)

app.run()