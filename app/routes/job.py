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

@job.route('/jobs/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_detail.html', job=job)




@job.route('/jobs/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_detail.html', job=job)




@job.route('/employer/dashboard')
@login_required
def employer_dashboard():
    if not current_user.is_employer:
        flash('Only employers can access the dashboard.')
        return redirect(url_for('job.list_jobs'))

    jobs = Job.query.filter_by(employer_id=current_user.id).all()
    return render_template('employer_dashboard.html', jobs=jobs)




@job.route('/jobs/<int:job_id>/edit', methods=['GET', 'POST'])
@login_required

def edit_job(job_id):
    job_obj = Job.query.get_or_404(job_id)
    
    if job_obj.employer_id != current_user.id:
        flash('You do not have permission to edit this job.', 'danger')
        return redirect(url_for('job.list_jobs'))





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
     