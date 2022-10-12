'''
This file stores the User model.
'''
from db import db


class UserModel(db.Model):
    '''
    This class defines the User model and contains user's attributes.
    '''
    __tablename__ = 'Users'

    user_id = db.Column(db.String(100), primary_key=True)
    acc_name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    profile_photo = db.Column(db.String(120))
    about = db.Column(db.String(300))
    address = db.Column(db.String(300))
    postal_code = db.Column(db.String(10))

    def __init__(self, user_id, acc_name, first_name, last_name,
                 password, email, balance, profile_photo, about,
                 address, postal_code) -> None:
        '''
        This function is the User class constructor.
        '''
        self.user_id = user_id
        self.acc_name = acc_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.balance = balance
        self.profile_photo = profile_photo
        self.about = about
        self.address = address
        self.postal_code = postal_code

    def __repr__(self) -> str:
        '''
        This function returns the User object representation in string format.
        '''
        return '<User %r>' % self.acc_name
