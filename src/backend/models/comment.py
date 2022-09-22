from db import db

class CommentModel(db.Model):
  __tablename__ = 'Comments'
  
  comment_id  = db.Column(db.String(100), primary_key=True)
  review_id = db.Column(db.String(100), db.ForeignKey('Reviews.review_id'))
  comment_date = db.Column(db.DateTime)
  comment_text = db.Column(db.Text)
  
  
  def __init__(self, comment_id, review_id, comment_date, comment_text) -> None:
    self.comment_id  = comment_id
    self.review_id = review_id
    self.comment_date = comment_date
    self.comment_text = comment_text