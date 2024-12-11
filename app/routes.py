from app import app, db
from flask import render_template ,request ,flash ,redirect ,url_for,session
from app.models import User
from app.form import SignUp, Login

@app.route('/debug-session') #for debug purposes delete when in production
def debug_session():
    print(f"Current session data: {session}")
    return f'Current session data: {session}'



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp(request.form)
    if 'userid' in session:
        flash('You are already logged in', 'success')
        return redirect(url_for('dashboard'))

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if user or email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('signup'))
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'error')
            return redirect(url_for('signup'))

        # Save user with hashed password
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Hash the password
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully! You may now log in', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)



@app.route('/login',methods=['GET','POST'])
def login():
    if 'userid' in session:
        flash('You are already logged in','success')
        return redirect(url_for('dashboard'))
    if request.method == 'GET':
        fein =  Login(request.form)
        return render_template('login.html',form=fein)
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['userid'] = user.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        
        elif user:
            flash('Invalid password','error')
            return redirect(url_for('login'))
        
        elif not user:
            flash('User does not exist','error')
            return redirect(url_for('login'))
        else:
            flash('Invalid credentials','error')
            return redirect(url_for('login'))
        
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out','success')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'userid' not in session:
        flash('You need to login first','error')
        return redirect(url_for('login'))
    user =User.query.filter_by(id=session['userid']).first()

    return render_template('dashboard.html',user=user)