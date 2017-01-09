from flask import Flask, render_template, request, redirect
from flask import url_for, session, flash, g

from functools import wraps

import sqlite3


app = Flask(__name__)
app.secret_key = 'test'

app.database = 'simple.db'


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
    g.db = connect_db()
    cur = g.db.execute('SELECT * FROM posts;')

    post_dict = {}
    posts = []
    for row in cur:
        post_dict['title'] = row[0]
        post_dict['description'] = row[1]
        posts.append(post_dict)

    g.db.close()
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

def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')