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
    # id of the review the user has left, if ther is any
    review_id = db.Column(db.Integer, db.ForeignKey(
        "Reviews.review_id"), unique=True)
    # id of the comment the user has left, if there is any
    comment_id = db.Column(db.Integer, db.ForeignKey(
        "Comments.comment_id"), unique=True)
    # id of the transaction, if a user has any
    tsc_id = db.Column(db.Integer, db.ForeignKey(
        "Transactions.transaction_id"), unique=True)
    # id of property posted, if a user has any
    property_id = db.Column(db.Integer, db.ForeignKey(
        "Properties.property_id"))
    # user's account name
    acc_name = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    profile_photo = db.Column(db.String(120))
    about = db.Column(db.String(300))

    def __init__(self, user_id, review_id, comment_id, tsc_id, property_id, acc_name,
                 first_name, last_name, password, email, balance, profile_photo, about) -> None:
        '''
        This function is the User class constructor.
        '''
        self.user_id = user_id
        self.review_id = review_id
        self.comment_id = comment_id
        self.tsc_id = tsc_id
        self.property_id = property_id
        self.acc_name = acc_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.balance = balance
        self.profile_photo = profile_photo
        self.about = about

    def __repr__(self):
        '''
        This function returns the User object representation in string format.
        '''
        return '<User %r>' % self.acc_name
