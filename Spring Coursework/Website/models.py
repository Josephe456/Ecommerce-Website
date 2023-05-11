from . import db
from flask_sqlalchemy import SQLAlchemy
from flask import session

#Database for products
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) #Product name
    price = db.Column(db.Integer) #Price
    description = db.Column(db.String(250)) #Product description
    envImpact = db.Column(db.String(250)) #Environmental impact description
    image = db.Column(db.String(250)) #Path to imge file

    def __repr__(self):
        return f'Item {self.name}'
