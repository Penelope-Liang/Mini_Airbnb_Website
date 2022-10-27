from qbay import app
from qbay.controllers import authenticate

"""
This file runs the server at a given port
"""

FLASK_PORT = 8080

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)

    @app.route('/', endpoint='home')
    @authenticate
    def home():
        return
