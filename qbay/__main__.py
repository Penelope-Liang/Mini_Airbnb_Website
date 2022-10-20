from qbay.controllers import *
from qbay import *
from qbay import app

"""
This file runs the server at a given port
"""

FLASK_PORT = 8080

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)
