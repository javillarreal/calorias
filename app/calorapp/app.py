from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = Config.DEBUG
db = SQLAlchemy(app)

import settings
import requests

#from models import User

@app.route("/")
def hello():
    return "Habla mani"

if __name__ == '__main__':
    app.run()
