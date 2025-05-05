from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import db
from app.models import Job
from app.forms import JobForm 


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

    form = JobForm()
    if form.validate_on_submit():
        new_job = Job(
            title=form.title.data,
            company=form.company.data,
            location=form.location.data,
            description=form.description.data
        )
        db.session.add(new_job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('job.list_jobs'))

    return render_template('post_job.html', form=form)
     