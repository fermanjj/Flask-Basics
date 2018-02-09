"""Run this file and visit
    127.0.0.1:5000 on your browser.

This first example covers a basic route in flask
    and the debug feature for development.
"""
from flask import Flask

# use __name__ to help flask determine where exactly it's being run from
app = Flask(__name__)
app.debug = True  # turn off in production


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
