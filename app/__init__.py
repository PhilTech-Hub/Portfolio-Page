import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect unauthorized users to login page




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
    app.secret_key = secrets.token_hex(16)
    
    
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    
    # Avoid circular imports by placing this here
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load user by ID

    # Create the tables (if they don't exist)
    with app.app_context():
        db.create_all()  # This will create the tables defined in your models

    # Import and register Blueprint
    from app.routes import bp
    from app.auth_routes import auth_bp  # New Blueprint for Authentication
    
    app.register_blueprint(bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    



    return app
