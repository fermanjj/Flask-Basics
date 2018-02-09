"""Run this file and visit
    127.0.0.1:5000 on your browser.

This example covers the basics of templates in flask
    using Jinja2.
"""
from flask import (
    Flask, render_template_string,
    render_template
)

# use __name__ to help flask determine where exactly it's being run from
app = Flask(__name__)
app.debug = True  # turn off in production


@app.route('/')
def home():
    name = 'JJ'

    html = """
    <html>
        <head>
            <title>{{ name }}</title>
        </head>
        <body>
            <h1>Hello, {{ name }}!</h1>
        </body>
    </html>
    """

    return render_template_string(html, name=name)


@app.route('/name/<string:name>')
def name_route(name):
    return render_template('name-ex2.html', name=name.title())


if __name__ == '__main__':
    app.run()
