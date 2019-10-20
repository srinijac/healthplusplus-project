# views.py

from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     # if form.validate_on_submit():
#     #     flash('Login requested for user {}, remember_me={}'.format(
#     #         form.username.data, form.remember_me.data))
#     #     return redirect(url_for('index.html'))
#     return render_template('login.html', title='Sign In', form=form)

@app.route('/login')
def login():
    return render_template("thissucks.html")
