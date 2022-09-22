from db import db

class AvaModel(db.Model):
  __tablename__ = 'Availabilities'
  
  ava_id  = db.Column(db.String(100), primary_key=True)
  property_id = db.Column(db.String(100), db.ForeignKey('Properties.prop_id'))
  start_date = db.Column(db.DateTime)
  end_date = db.Column(db.DateTime)
  
  def __init__(self, ava_id, property_id, 
               start_date, end_date) -> None:
    self.ava_id  = ava_id
    self.property_id = property_id
    self.start_date = start_date
    self.end_date = end_date