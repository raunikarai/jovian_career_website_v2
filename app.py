from flask import Flask,render_template, jsonify#importing Flask class from class library
app=Flask(__name__)

JOBS=[{
    'id':1,
    'title':'Data Analyst',
    'Location':'Bengluru,India',
    'Salary':'10,00,000',
    },
{
    'id':2,
    'title':'Data Scientist',
    'Location':'Bengluru,India',
    'Salary':'15,00,000',
},
{
    'id':3,
    'title':'Frontend Engineer',
    'Location':'Delhi,India',
    'Salary':'1,00,000',
},
{
    'id':4,
    'title':'Backend Engineer',
    'Location':'Chennai,India',
    'Salary':'1,00,000',
}]


@app.route("/")
def hello_world(): #running this fuction whenver some one open the browser 
    return render_template('home.html',jobs=JOBS, company_name='Jovian')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS) #my web server is not only returing a HTML page but also returning the information in the for of json 

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)