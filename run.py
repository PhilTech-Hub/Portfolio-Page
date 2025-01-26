from app import create_app, db


app = create_app()

# Ensure that the application context is set
try:
    with app.app_context():
        db.create_all()
        print("Database initialized successfully.")
except Exception as e:
    print(f"Error initializing database: {e}")


    
if __name__ == "__main__":
    app.run(debug=True)
