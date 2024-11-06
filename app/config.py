# app/config.py

import os

class Config:
    # Database configuration - SQLite
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://daven:03D%40ven11@116.86.77.68:3306/appdev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
