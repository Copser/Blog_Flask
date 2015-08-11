# blog.py - controller
from functools import wraps
import sqlite3
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g


# database configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xe9\xcd\x04%q\xe2\xe6\xee\x14\xe4#xy\x89\xef\x8c\xd6E\xa4\xc3\x166#'
app = Flask(__name__)

# pulls in app configuration by looking for  UPERCASE veriables
app.config.from_object(__name__)


# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap


# Adding function for are views
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or\
                request.form['password'] != app.config['PASSWORD']:
            error = "Invalid Credentials. Please try again!"
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)


@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute("select * from posts")
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', posts=posts)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You where logged out!')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
