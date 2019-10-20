# app/__init__.py

from flask import Flask
from config import Config

# initialize the app
# load the config file
app = Flask(__name__)
app.config.from_object(Config)

# load the views
from app import views
