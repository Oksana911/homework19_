from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.user import User
from setup_db import db

from views.directors import *
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns

def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)


def create_app(config_object):
    application = Flask(__name__)
    register_extensions(application)
    application.config.from_object(config_object)
    return application


if __name__ == '__main__':
    app = create_app(Config())
    app.run(host="localhost", port=10001, debug=True)
