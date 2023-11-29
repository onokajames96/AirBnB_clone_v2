#!/usr/bin/python3
"""Imports the Flask class from the Flask module."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Defines the hello_hbnb""""

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
