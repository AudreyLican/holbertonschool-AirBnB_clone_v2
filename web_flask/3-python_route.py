#!/usr/bin/python3
"""Starting a web application with Flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>, strict_slashes=False')
def c_text(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<string:text>, strict_slashes=False')
def python_text(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
