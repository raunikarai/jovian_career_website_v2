from flask import Flask,render_template, jsonify#importing Flask class from class library
from database import load_jobs_from_db, load_job_from_db
app=Flask(__name__)
                 
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

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)