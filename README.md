# Job-Board-Flask

🔧 Step 1: System Design
🧩 Features of the Job Board:
Job Listings Page

Job Detail Page

Admin Job Posting Interface

Search and Filter Jobs

Apply for a Job (Optional: File Upload for CV)

Database for Jobs and Applications

🗃️ Database Tables (using SQLite for simplicity):
jobs

id: integer (PK)

title: string

company: string

location: string

description: text

date_posted: datetime

applications (optional)

id: integer (PK)

job_id: foreign key

applicant_name: string

email: string

cv_filename: string