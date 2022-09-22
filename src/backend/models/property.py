from db import db

class PropertyModel(db.Model):
  __tablename__ = 'Properties'
  
  prop_id  = db.Column(db.String(100), primary_key=True)
  
  def __init__(self, prop_id) -> None:
    self.prop_id  = prop_id