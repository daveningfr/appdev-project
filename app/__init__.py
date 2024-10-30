from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config  # Import the config

# Initialize the app
app = Flask(__name__)
# Apply configuration
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)


# Import routes after initializing `app`
from app import routes
