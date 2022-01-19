# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    c = "<h1>Hello World!</h1>"
    #return "Hello World!"
    return c