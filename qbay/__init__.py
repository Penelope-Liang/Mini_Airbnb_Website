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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '69cae04b04756f65eabcd2c5a11c8c24'
app.app_context().push()
