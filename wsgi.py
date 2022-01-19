# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    c = "<h1>Hello World!</h1>"
    #return "Hello World!"
    return c

@app.route("/api/v1/products")
def products():
    PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv'},
    3: { 'id': 3, 'name': 'Le Wagon'},
}
    return PRODUCTS