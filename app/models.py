from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    technologies = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # initiated, in-progress, completed

class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    issued_by = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(200), nullable=False)
