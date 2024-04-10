#!/usr/bin/python3
"""Starting a web application with Flask"""
from flask import Flask


app = Flask(__name__)

#route to display Hello HBNB!
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

#route to display HBNB
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

#route to display 'C <text>'
@app.route('/c/<text>, strict_slashes=False')
def c_text(text):
    return "C {}".format(text.replace('_', ' '))

#route to display 'Python <text>'
@app.route('/python/<text>, strict_slashes=False')
def python_text(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))

#route to display '<n> is a number'
@app.route('/number/<n>, strict_slashes=False')
def number_n(n:int):
    return "{} is a number".format(n)


if __name__ == '__main__':
    #run the flask app
    app.run(host='0.0.0.0', port=5000)
