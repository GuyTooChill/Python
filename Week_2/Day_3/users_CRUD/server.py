from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
from users import User

app = Flask(__name__)    

# -----------------------------------------------------------
@app.route('/')         
def read_users():
    all_users = User.show_users()
    return render_template ("read.html", all_users = all_users)



@app.route('/create')         
def create_users():
    return render_template ("create.html")

@app.route('/submit', methods = ['post'])         
def submit_users():
    User.create_user(request.form)
    return redirect ("/")



if __name__=="__main__":    
    app.run(debug=True)    