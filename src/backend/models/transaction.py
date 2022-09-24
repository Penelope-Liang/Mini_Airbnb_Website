from db import db

class TscModel(db.Model):
  __tablename__ = 'Transactions'
  
  tsc_id  = db.Column(db.String(100), primary_key=True)
  user_id = db.Column(db.String(100), db.ForeignKey('Users.user_id'))
  property_id = db.Column(db.String(100), db.ForeignKey('Properties.prop_id'))
  tsc_date = db.Column(db.DateTime)
  tsc_price = db.Column(db.Float(precision=2))
  check_in_date = db.Column(db.DateTime)
  check_out_date = db.Column(db.DateTime)
  guest_number = db.Column(db.Integer)
  
  def __init__(self, tsc_id, user_id, property_id,tsc_data,tsc_price,
               check_in_date, check_out_date, guest_number) -> None:
    self.tsc_id  = tsc_id
    self.user_id = user_id
    self.property_id = property_id
    self.tsc_data = tsc_data
    self.tsc_price = tsc_price
    self.check_in_date = check_in_date
    self.check_out_date = check_out_date
    self.guest_number = guest_number
    
  def __repr__(self):
        return '<Transactions %r>' % self.title
    