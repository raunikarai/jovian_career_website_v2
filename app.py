from flask import Flask,render_template #importing Flask class from class library
app=Flask(__name__)

@app.route("/")
def hello_world(): #running this fuction whenver some one open the browser 
    return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)