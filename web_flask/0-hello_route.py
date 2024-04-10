#!/usr/bin/python3
"""Starting a web application with Flask"""
from flask import Flask


app = Flask(__name__)

#define route
@app.route('/', strict_slashes=False)
def hello():
    #display a message Hello HBNB!
    return "Hello HBNB!"


if __name__ == '__main__':
    #run the flask app
    app.run(host='0.0.0.0', port=5000)
