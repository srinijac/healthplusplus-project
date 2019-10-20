# views.py

from flask import Flask, render_template, request, flash, redirect, url_for
import json
from app.forms import LoginForm
from app import app
from app import tr
from app.tr import sendsms

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
def smstest():
    first = request.values.get("first_name")
    last = request.values.get("last_name")
    tr.sendsms(first, last)
    # os.system('python tr.py')
    return render_template("index.html")
