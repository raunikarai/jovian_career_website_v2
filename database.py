from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
    with engine.connect() as conn:
     result=conn.execute(text("select * from JOBS"))
     jobs=[]
    for row in result.all():
         jobs.append(dict(row._mapping))
    return jobs
        
        
def load_job_from_db(id):
     with engine.connect() as conn:
          result=conn.execute(text("select * from JOBS where ID = :val"),{"val": id})
          row = result.fetchone()  # Fetch just one row

     if row is None:
        return None
     else:
        return dict(row._mapping) 
     
def add_application_to_db(job_id, data, resume_path):
    with engine.begin() as conn:  # use `begin()` instead of `connect()`
        query = text("""
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_path)
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_path)
        """)
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "work_experience": data['work_experience'],
            "resume_path": resume_path
        })

