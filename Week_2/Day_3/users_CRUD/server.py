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



@app.route('/show/<int:id>')         
def show_users(id):
    user_data = {'id' : id}
    one_user = User.one_user(user_data)
    return render_template ("show.html", one_user = one_user)



@app.route('/edit/<int:id>')         
def edit_users(id):
    user_data = {'id' : id}
    one_user = User.one_user(user_data)
    return render_template ("edit.html", one_user = one_user)

@app.route('/change/<int:id>', methods = ['post'])         
def change_users(id):
    user_data = {
        "id" : id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.change_user(user_data)
    return redirect (f"/show/{id}" )



@app.route('/delete/<int:id>')         
def delete_users(id):
    user_data = {'id' : id}
    User.delete_user(user_data)
    return redirect ("/")



if __name__=="__main__":    
    app.run(debug=True)    