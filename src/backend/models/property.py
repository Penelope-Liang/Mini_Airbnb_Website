'''
This file stores the Propety model
'''

from db import db


class PropertyModel(db.Model):
    '''
    The class defines the Property model and contains Property attributes.
    '''
    __tablename__ = 'Properties'

    # set property id as primary key and String
    prop_id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey("Users.user_id"))
    posted_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(120), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __init__(self, prop_id, user_id, posted_date,
                 title, description, image, price, address, capacity) -> None:
        '''
        This class initialize Property attributes.
        '''
        self.prop_id = prop_id
        self.user_id = user_id
        self.posted_date = posted_date
        self.title = title
        self.description = description
        self.image = image
        self.price = price
        self.capacity = capacity
        self.address = address

    def __repr__(self) -> str:
        return '<Property %r>' % self.title
