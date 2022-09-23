'''
This file contains sql model for property class
'''

from db import db


class PropertyModel(db.Model):
    __tablename__ = 'Properties'

    # set property id as primary key and String
    prop_id = db.Column(db.String(100), primary_key=True)
    # user_id and availability_id is foreign key
    user_id = db.Column(db.String(100), db.ForeignKey("User.user_id"))
    availability_id = db.Column(db.String(100),
                                db.ForeignKey("Availability.availability_id"))
    posted_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    capacoity = db.Column(db.Integer, nullable=False)

    def __init__(self, prop_id, user_id, availability_id, posted_date,
                 title, description, image, price, address, capacoity) -> None:
        self.prop_id = prop_id
        self.user_id = user_id
        self.availability_id = availability_id
        self.posted_date = posted_date
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.capacoity = capacoity
        self.address = address

    def __repr__(self):
        return '<Property %r>' % self.title
