from wtforms import Form, StringField, validators,EmailField,PasswordField

class SignUp(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = EmailField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [validators.Length(min=6, max=35),validators.DataRequired()])


class Login(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
