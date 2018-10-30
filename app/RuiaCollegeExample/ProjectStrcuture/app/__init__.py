# app/__init__.py

from flask import Flask
from flask_bootstrap import Bootstrap
#from config import app_config

# Initialize the app
app = Flask(__name__)
bootstrap= Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
SECRET_KEY = 'hard to guess string'

