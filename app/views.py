# views.py

from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app import app

#twilio
from twilio.rest import Client
import cgi
import cgitb

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("thissucks.html")

@app.route('/sms')
def message():
    inputs = cgi.FieldStorage()

    first_name = inputs.getvalue('first_name').capitalize()
    last_name  = inputs.getvalue('last_name').capitalize()

    # Your Account SID from twilio.com/console
    account_sid = "ACa3ee54b5030f3a2b427107e4ff8517af"
    # Your Auth Token from twilio.com/console
    auth_token  = "5f5479d1ea747a53454b61d812376cc4"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+14074373965",
        from_="+12052930681",
        body=("your name is", first_name, last_name)

    # return render_template("index.html")
