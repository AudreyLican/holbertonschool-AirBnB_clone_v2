#!/usr/bin/python3
"""Starting a web application with Flask"""
from flask import Flask, render_template

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
@app.route('/python/<string:text>, strict_slashes=False')
def python_text(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    #run the flask app
    app.run(host='0.0.0.0', port=5000)
