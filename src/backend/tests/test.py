from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tests/data.db'

@app.before_first_request
def create_tables():
  print("=================tables are created======================")
  db.create_all()


if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port=8000, debug=True)