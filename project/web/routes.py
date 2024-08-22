from flask import Flask, render_template, request, redirect, url_for
from connect import connection
from db import check
import random

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_fail')
def login_fail():
    return render_template('login_fail.html')

@app.route('/tour')
def tour():
    return render_template('tour.html')


@app.route('/login_check',methods = ['post'])
def login_check():
    id_ = request.form['id_']
    pw_ = request.form['pw_']
    users = check(id_, pw_)
    if users:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_fail'))

if __name__=='__main__':
    app.run(debug=True)