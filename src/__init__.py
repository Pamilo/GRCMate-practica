from flask import Flask
# Import the app instance from puentes.py


def aplication_init():
    app = Flask(__name__)
    # Mount at /api
    return app

