import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)

    # Create the 'instance' folder if it doesn't exist
    instance_folder = os.path.join(os.getcwd(), 'instance')
    os.makedirs(instance_folder, exist_ok=True)
    if not os.access(instance_folder, os.W_OK):
        raise PermissionError(f"Instance folder {instance_folder} is not writable.")

    # Get and normalize the DATABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        # Convert old scheme to new one (required for SQLAlchemy compatibility)
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    else:
        db_path = os.path.join(instance_folder, 'portfolio.db')
        database_url = f'sqlite:///{db_path}'  # fallback

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Debugging information
    print(f"Instance folder: {instance_folder}")
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Set the secret key
    app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    if 'SECRET_KEY' not in os.environ:
        print("Warning: SECRET_KEY not found in environment, using a randomly generated key.")

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # Avoid circular imports by placing this here
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import and register Blueprints
    from app.routes import bp
    from app.auth_routes import auth_bp
    app.register_blueprint(bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
