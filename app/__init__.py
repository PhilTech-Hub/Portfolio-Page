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
    # Create Flask app with instance-relative config for instance/ folder
    app = Flask(
        __name__,
        instance_relative_config=True,
    )

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        raise RuntimeError(f"Failed to create instance folder: {e}")

    # Load DATABASE_URL from .env or use SQLite fallback
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        # Normalize Heroku-style postgres URL
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
    else:
        db_path = os.path.abspath('portfolio.db')  # Save DB in project root
        print(f"Using DB path: {db_path}")
        database_url = f"sqlite:///{db_path}"



    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set Flask environment if not already defined
    app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

    # Set a secret key for session management
    app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(16))
    if not os.getenv('SECRET_KEY'):
        print("Warning: SECRET_KEY not found in .env. A random one is being used.")

    # Debug output
    print(f"Instance path: {app.instance_path}")
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # Import models to register with SQLAlchemy
    from app.models import User  # Make sure app/models.py defines User model

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes import bp  # Make sure app/routes.py defines bp = Blueprint(...)
    from app.auth_routes import auth_bp  # Make sure app/auth_routes.py defines auth_bp = Blueprint(...)
    app.register_blueprint(bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')



    return app
