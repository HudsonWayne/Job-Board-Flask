from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Job


job = Blueprint('job', __name__)


@job.route('/jobs')
def list_jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)



@job.route('/jobs/post', methods=['GET', 'POST'])
@login_required
def post_job():
    if not current_user.is_employer:
        flash('Only employers can post jobs.')
        return redirect(url_for('job.list_jobs'))
