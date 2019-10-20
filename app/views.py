# views.py

from flask import Flask, render_template, request, flash, redirect, url_for
import json
from app.forms import LoginForm
from app import app
from app import tr
from app.tr import sendsms, addnumber

#twilio
from twilio.rest import Client
import cgi
import cgitb
import os
from subprocess import Popen

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/tr', methods=['GET', 'POST'])
def login():
    first = request.values.get("first_name")
    last = request.values.get("last_name")
    number = request.values.get("to_phone_num")
    message = "You're signed up! Welcome to ___, %s %s%s%s!"
    print(number)
    #tr.addnumber(number)
    tr.sendsms(message, number first, last)
    # os.system('python tr.py')
    return render_template("index.html")
