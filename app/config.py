from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF protection
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)