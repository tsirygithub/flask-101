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

@app.route("/api/v1/produits")
def get_current_user():
    return jsonify(
        username=g.user.username,
        email=g.user.email,
        id=g.user.id,
    )