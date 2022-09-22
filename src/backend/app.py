from flask import Flask
from flask_restful import Api
from models.user import UserModel
from models.property import PropertyModel
from models.transaction import TscModel
from models.review import ReviewModel
from models.comment import CommentModel
from models.availability import AvaModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
  '''
    The function only be trigger when first time access 
    through http, and then it will create all of the tables
    in the models directory.
  '''
  print("=================tables are created======================")
  db.create_all()

# api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port=2555, debug=True)