import re
from wtforms import Form, StringField, validators, EmailField, PasswordField, ValidationError

def password_complexity_check(form, field):
    password = field.data
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.search(r'[0-9]', password):
        raise ValidationError('Password must contain at least one number.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('Password must contain at least one symbol.')

class SignUp(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = EmailField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.Length(min=8),
        validators.DataRequired(),
        password_complexity_check
    ])
    confirm = PasswordField('Repeat Password', [
        validators.EqualTo('password', message='Passwords must match'),
        validators.DataRequired()
    ])

class Login(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
