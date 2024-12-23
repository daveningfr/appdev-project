from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from dotenv import load_dotenv
import os
from corbado_python_sdk import CorbadoSDK , Config as corbado_config


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF protection
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    CORBADO_CLIENT_SECRET = os.getenv('API_SECRET')
    CORBADO_PROJECT_ID = os.getenv('PROJECT_ID')

app = Flask(__name__)
app.config.from_object(Config)
corbado = corbado_config(project_id = Config.CORBADO_PROJECT_ID, api_secret = Config.CORBADO_CLIENT_SECRET)
sdk = CorbadoSDK(config=corbado)

db = SQLAlchemy(app)