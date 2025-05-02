from .. import db  # Relative import to avoid circular import
from datetime import datetime
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_employer = db.Column(db.Boolean, default=False)
    jobs = db.relationship('JobPost', backref='employer', lazy=True)
