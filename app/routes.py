from app import app
from flask import render_template ,request
from app.form import SignUp


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    fein = SignUp(request.form)
    return render_template('signup.html', form=fein)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
