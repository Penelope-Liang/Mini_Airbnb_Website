'''
This file stores the User model.
'''
from qbay.db import db


class Users(db.Model):
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


class ReviewModel(db.Model):
    '''
    This class defines the Review Model
    and contains Review's attributes.
    '''

    __tablename__ = 'Reviews'
    review_id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey('Users.user_id'))
    comment_id = db.Column(db.String(100),
                           db.ForeignKey('Comments.comment_id'))
    property_id = db.Column(db.String(100),
                            db.ForeignKey('Properties.prop_id'))
    rating = db.Column(db.Float(precision=2))
    review_date = db.Column(db.DateTime)
    title = db.Column(db.Text)
    review_text = db.Column(db.Text)

    def _init_(self, review_id,
               user_id, comment_id,
               property_id,
               rating, review_date,
               title, review_text) -> None:
        self.review_id = review_id
        self.user_id = user_id
        self.comment_id = comment_id
        self.property_id = property_id
        self.rating = rating
        self.review_date = review_date
        self.title = title
        self.review_text = review_text

    def __repr__(self) -> str:
        '''
        This class returns a string as a representation of the Review.
        '''
        return '<Review %r>' % self.review_id


class AvaModel(db.Model):
    '''
    This class defines the Availability Model
    and contains Availability's attributes.
    '''
    __tablename__ = 'Availabilities'
    ava_id = db.Column(db.String(100), primary_key=True)
    property_id = db.Column(db.String(100),
                            db.ForeignKey('Properties.prop_id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __init__(self, ava_id, property_id, start_date, end_date) -> None:
        self.ava_id = ava_id
        self.property_id = property_id
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self) -> str:
        '''
        This class returns a string as a representation of the Availability.
        '''
        return '<Availability %r>' % self.ava_id


class CommentModel(db.Model):
    '''
    This class defines the comment model
    and contains comment's attributes.
    '''

    __tablename__ = 'Comments'
    comment_id = db.Column(db.String(100), primary_key=True)
    comment_date = db.Column(db.DateTime)
    comment_text = db.Column(db.Text)

    def __init__(self, comment_id,
                 comment_date, comment_text) -> None:
        '''
        This class initialize Comment's attributes.
        '''
        self.comment_id = comment_id
        self.comment_date = comment_date
        self.comment_text = comment_text

    def __repr__(self) -> str:
        '''
        This class returns a string as a
        representation of the Comment.
        '''
        return '<Comment %r>' % self.comment_id


class PropertyModel(db.Model):
    '''
    The class defines the Property model and contains Property attributes.
    '''
    __tablename__ = 'Properties'

    # set property id as primary key and String
    prop_id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey("Users.user_id"))
    posted_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(3000), nullable=False)
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


class TscModel(db.Model):
    '''
    This class defines the Transactions model
    and contains Transaction's attributes.
    '''

    __tablename__ = 'Transactions'
    tsc_id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.String(100), db.ForeignKey('Users.user_id'))
    property_id = db.Column(db.String(100),
                            db.ForeignKey('Properties.prop_id'))
    tsc_date = db.Column(db.DateTime)
    tsc_price = db.Column(db.Float(precision=2))
    check_in_date = db.Column(db.DateTime)
    check_out_date = db.Column(db.DateTime)
    guest_number = db.Column(db.Integer)

    def __init__(self, tsc_id, user_id, property_id, tsc_data,
                 tsc_price, check_in_date, check_out_date,
                 guest_number) -> None:
        '''
        This class initialize Transaction's attributes.
        '''
        self.tsc_id = tsc_id
        self.user_id = user_id
        self.property_id = property_id
        self.tsc_data = tsc_data
        self.tsc_price = tsc_price
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.guest_number = guest_number

        db.create_all()

    def __repr__(self):
        '''
        This class returns a string as a representation of the Transactions.
        '''
        return '<Transactions %r>' % self.title
