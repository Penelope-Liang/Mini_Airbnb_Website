from db import db

class TscModel(db.Model):
  __tablename__ = 'Transactions'
  
  tsc_id  = db.Column(db.String(100), primary_key=True)
  
  def __init__(self, tsc_id) -> None:
    self.tsc_id  = tsc_id