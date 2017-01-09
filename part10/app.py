from flask import Flask, render_template, request, redirect
from flask import url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

from functools import wraps


app = Flask(__name__)


import os
app.config.from_object(os.environ.setdefault('APP_SETTINGS','config.BaseConfig'))
# app.config.from_object(os.environ['APP_SETTINGS])
# app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
from models import *


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials, Please try again.'
        else:
            session['logged_in'] = True
            flash('You had log in now!')
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You had log out now!')
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')