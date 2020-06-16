from flask import Flask
from database.db import initialize_db
from flask_restful import Api 
from resources.routes import initialize_routes 

app = Flask(__name__)
api = Api(app)

# movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
#         "genres": ["Drama"]
#     },
#     {
#        "name": "The Godfather ",
#        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
#        "genres": ["Crime", "Drama"]
#     }
# ]


app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/movie-bag'
}
initialize_db(app)

initialize_routes(api)

app.run()


# if __name__ == '__main__':
#     app.run(debug=True)