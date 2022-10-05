from flask_sqlalchemy import SQLAlchemy
from multiprocessing import connection
import sqlite3

# connect to the database
# connection = sqlite3.connect('./data.db')
# cursor = connection.cursor()
db = SQLAlchemy()
