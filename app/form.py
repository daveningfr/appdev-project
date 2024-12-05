from wtforms import Form, StringField, validators

class SignUp(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.DataRequired()])
    password = StringField('New Password', [validators.Length(min=6, max=35),validators.DataRequired()])
