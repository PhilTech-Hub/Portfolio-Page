from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_path = os.path.abspath('test.db')
print(f"DB Path: {db_path}")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Dummy(db.Model):
    id = db.Column(db.Integer, primary_key=True)

with app.app_context():
    db.create_all()
