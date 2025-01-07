from app import db


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
