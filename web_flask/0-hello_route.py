#!/usr/bin/python3
"""Starting a web application with Flask"""
from flask import Flask

app = Flask(__name__)


#route to display Hello HBNB!
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    #run the flask app
    app.run(host='0.0.0.0', port=5000)
