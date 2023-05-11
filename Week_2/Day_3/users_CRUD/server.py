from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)    

# -----------------------------------------------------------
@app.route('/')         
def read_users():
    return render_template ("read.html")


@app.route('/create')         
def create_users():
    return render_template ("create.html")

@app.route('/submit')         
def submit_users():
    return redirect ("/")



# -------------------------------------------------------------
class User:
    def __init__(self) -> None:
        pass





if __name__=="__main__":    
    app.run(debug=True)    