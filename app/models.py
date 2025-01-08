from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    technologies = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Project {self.name}>'

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    issued_by = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Optional, but recommended for clarity
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, password):
        """Hashes the password and sets it."""
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        """Checks the password against the stored hash."""
        return check_password_hash(self.password, password)