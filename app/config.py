from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF protection
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)