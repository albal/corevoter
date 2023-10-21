'''
This file contains the database models for our application.
'''
from app import db
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    votes = db.Column(db.Integer, default=0)
    status = db.Column(db.String(120), default='Open')
    # More fields can be added here as per requirements