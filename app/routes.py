from app import app, db
from flask import render_template ,request ,flash ,redirect ,url_for    
from app.models import User
from app.form import SignUp


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    fein = SignUp(request.form)
    return render_template('signup.html', form=fein)

@app.route('/signup', methods=['POST'])
def signup_submit():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if user or email already exists
    if User.query.filter_by(email=email).first():
        flash('Email already exists.','error')
        return redirect(url_for('signup'))
    if User.query.filter_by(username=username).first():
        flash('Username already exists.','error')
        return redirect(url_for('signup'))
    # Save user with hashed password
    new_user = User(username=username, email=email)
    new_user.set_password(password)  # Hash the password
    db.session.add(new_user)
    db.session.commit()

    flash('User registered successfully!', 'success')
    return redirect(url_for('signup'))

@app.route('/login')
def login():
    return render_template('login.html')
