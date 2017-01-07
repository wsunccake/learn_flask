from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'


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
            return redirect(url_for('home'))

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')