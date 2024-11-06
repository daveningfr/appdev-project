from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from app.config import Config  # If configurations are in a separate file

app = Flask(__name__)
app.config.from_object(Config)

# Initialize a connection function
# def get_db_connection():
#     return pymysql.connect(
#         host=app.config['MYSQL_HOST'],
#         user=app.config['MYSQL_USER'],
#         password=app.config['MYSQL_PASSWORD'],
#         database=app.config['MYSQL_DB'],
#         cursorclass=pymysql.cursors.DictCursor  # For dictionary-like rows
#     )
