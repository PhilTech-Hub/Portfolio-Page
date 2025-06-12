from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)  # Changed from String(200)
    technologies = db.Column(db.Text, nullable=False)  # Changed from String(200)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Project {self.name}>'


class Certification(db.Model):
    __tablename__ = 'certifications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    issued_by = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Certification {self.title}>'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'
