# app/__init__.py

from flask import Flask
from config import Config

# initialize the app
app = Flask(__name__, instance_relative_config = True)

# load the views
from app import views
from app import routes

# load the config file
app.config.from_object('config')
