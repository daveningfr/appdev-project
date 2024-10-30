from flask import Flask

# Initialize the app
app = Flask(__name__)

# Import routes after initializing `app`
from app import routes
