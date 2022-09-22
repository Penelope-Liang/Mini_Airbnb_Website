from db import db


class UserModel(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, user_id) -> None:
        self.user_id = user_id