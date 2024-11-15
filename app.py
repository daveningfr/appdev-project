from app import app, db

if __name__ == '__main__':
    # Create tables within the app context
    with app.app_context():
        db.create_all()
    
    # Run the app
    app.run(debug=True)

