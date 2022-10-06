from db import db
from flask import Flask, render_template
from flask_smorest import Api
from models import UserModel
from models import PropertyModel
from models import TscModel
from models import ReviewModel
from models import CommentModel
from models import AvaModel
from resources.userRegister import blp as RegisterBluePrint


def create_app(db_url=None):
    app = Flask(__name__, template_folder="../frontend")
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
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

    api.register_blueprint(RegisterBluePrint)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
