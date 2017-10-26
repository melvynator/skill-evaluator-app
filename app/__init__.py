# Import datetime
import datetime

# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Import a module / component using its blueprint handler variable (mod_auth)
from app.controllers.search import search

# from theSwitchAPI.controllers.accounts.authentification import authentication_endpoint

# Sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(search)

# app.register_blueprint(authentication_endpoint)
