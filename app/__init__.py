from flask import Flask

#Initializing application
app = Flask(__name__, instance_relative_config=True)

#Setting up configuration
app.config.from_object('config')

from app import views