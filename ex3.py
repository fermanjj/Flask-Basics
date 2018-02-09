"""Run this file and visit
    127.0.0.1:5000 on your browser.

This example goes over persistent data and
    more advanced templating techniques.
"""
from flask import (
    Flask, render_template, request,
    flash, redirect, url_for
)

# use __name__ to help flask determine where exactly it's being run from
app = Flask(__name__)
app.debug = True  # turn off in production
app.secret_key = 'super-secret-key'


DATABASE = {'users': [{'username': 'test', 'password': 'test'}]}


@app.route('/')
def home():
    return render_template('home-ex3.html')


@app.route('/name', methods=['POST'])
def name_route():

    name = request.form['name']

    return render_template('name-ex3.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login-ex3.html')

    form_username = request.form['username']
    form_password = request.form['password']

    for u in DATABASE['users']:
        if form_username == u['username'] and form_password == u['password']:
            flash({'message': 'Logged in', 'alert': 'success'})
            return redirect(url_for('home'))

    flash({'message': 'Incorrect username or password', 'alert': 'danger'})
    return render_template('login-ex3.html')


if __name__ == '__main__':
    app.run()
