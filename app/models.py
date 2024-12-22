from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    green_points = db.Column(db.Integer, default=0)
    email_verified = db.Column(db.Boolean, default=False)
    email_token = db.Column(db.String(120), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def generate_email_token(self):
        self.email_token = secrets.token_urlsafe(32)
    
    

    def __repr__(self):
        return f'<User {self.username}>'
