import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Create the 'instance' folder if it doesn't exist
    instance_folder = os.path.join(os.getcwd(), 'instance')
    if not os.path.exists(instance_folder):
        os.makedirs(instance_folder)

    # Set the database path and URI
    db_path = os.path.join(instance_folder, 'portfolio.db')
    print(f"Database path: {db_path}")  # Debugging line to print the path

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Create the tables (if they don't exist)
    with app.app_context():
        db.create_all()  # This will create the tables defined in your models

    # Import and register Blueprint
    from app.routes import bp
    app.register_blueprint(bp)



    return app
