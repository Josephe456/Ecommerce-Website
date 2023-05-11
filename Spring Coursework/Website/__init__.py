from flask import Flask, Blueprint, request, session
from flask_sqlalchemy import SQLAlchemy
from os import path

#Sets name of the database
DB_NAME = "items.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Creates database table in instance
    db.init_app(app)

    #Imports the different paths from views
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Item

    create_database(app)

    return app

#Creates a database if one doesn't exist
def create_database(app):
    if not path.exists('Website/' + DB_NAME):
        with app.app_context():
            db.create_all()
