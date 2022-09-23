from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db

# setting up SQLAlchemy and data models so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    # id of the review the user has left
    review_id = db.Column(db.Integer, db.ForeignKey(
        "Review.review_id"), unique=True)
    # id of the transaction, if a user has any
    transaction_id = db.Column(db.Integer, db.ForeignKey(
        "Transaction.transaction_id"), unique=True)
    # id of property posted, if a user has any
    property_id = db.Column(db.Integer, db.ForeignKey(
        "Property.property_id"))
    username = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)
    profile_photo = db.Column(db.String(120))
    about = db.Column(db.String(300))

    def __repr__(self):
        return '<User %r>' % self.username
