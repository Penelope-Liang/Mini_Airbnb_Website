'''
an init file is required for this folder to be considered as a module
'''

from flask import Flask
import os
import sys
import pathlib

sys.path.append(pathlib.Path().resolve().__str__())
sys.path.append(pathlib.Path().resolve().joinpath("qbay").__str__())
sys.path.append(pathlib.Path().resolve().joinpath("qbay_test").__str__())

package_dir = os.path.dirname(
    os.path.abspath(__file__)
)


templates = os.path.join(
    package_dir, "templates"
)
db_path = os.path.join(package_dir, "data.db")
app = Flask(__name__)
# Docker Compose sets db_string to a MySQL URL; local runs use SQLite.
db_string = os.getenv('db_string')
if db_string:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_string
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '69cae04b04756f65eabcd2c5a11c8c24'
app.app_context().push()

from qbay.db import db  # noqa: E402
from qbay import models  # noqa: E402, F401

# Create any missing tables, e.g. on a fresh MySQL database.
db.create_all()
