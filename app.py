from flask import Flask,render_template, jsonify, request#importing Flask class from class library
from werkzeug.utils import secure_filename
import os
from database import load_jobs_from_db, load_job_from_db
from database import add_application_to_db

app=Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # make sure this folder exists
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
                 
@app.route("/")
def hello_world(): #running this fuction whenver some one open the browser 
    jobs=load_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs) 
#my web server is not only returing a HTML page but also returning the information in the for of json 

@app.route("/jobs/<id>")
def show_job(id):
    job=load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    data = request.form
    resume_file = request.files['resume']

    if resume_file and allowed_file(resume_file.filename):
        filename = secure_filename(resume_file.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(resume_path)

        # Save the application to DB
        add_application_to_db(id, data, resume_path)

        return render_template("application_submitted.html",
                               application=data,
                               resume_url=resume_path,
                               job=load_job_from_db(id))
    else:
        return "Invalid or missing resume file", 400



if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)