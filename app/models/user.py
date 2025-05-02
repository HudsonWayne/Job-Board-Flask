from .. import db  # Relative import to avoid circular import
from datetime import datetime
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_employer = db.Column(db.Boolean, default=False)
    jobs = db.relationship('JobPost', backref='employer', lazy=True)


class JobPost(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    applications = db.relationship('Application', backref='job', lazy=True)
    
    
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(150), nullable=False)
    applicant_email = db.Column(db.String(150), nullable=False)
    resume = db.Column(db.Text)  
    job_id = db.Column(db.Integer, db.ForeignKey('job_post.id'), nullable=False)