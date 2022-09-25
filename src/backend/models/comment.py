'''
This file contains sql model for comment class
'''

from db import db


class CommentModel(db.Model):
  '''
  This class defines the Comment Model
  and contains Comment's attributes.
  '''
  __tablename__ = 'Comments'
  comment_id  = db.Column(db.String(100), primary_key=True)
  review_id = db.Column(db.String(100), db.ForeignKey('Reviews.review_id'))
  comment_date = db.Column(db.DateTime)
  comment_text = db.Column(db.Text)
  
  def __init__(self, comment_id, review_id, 
               comment_date, comment_text) -> None:
    '''
    This class initialize Comment's attributes
    '''
    self.comment_id  = comment_id
    self.review_id = review_id
    self.comment_date = comment_date
    self.comment_text = comment_text
    
  def __repr__(self):
    '''
    This class returns a string as a representation of the Comment.
    '''
    return '<Comment %r>' % self.comment_id