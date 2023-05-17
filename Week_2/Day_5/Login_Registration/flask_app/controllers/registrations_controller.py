from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.registrations import Register
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/register', methods = ['post'])
def register():
    if not Register.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    newuser_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id = Register.create_user(newuser_data)
    session['user_id'] = user_id
    return redirect(f'/user/{user_id}')


@app.route('/login', methods = ['post'])
def login():
    email_data = {'email' : request.form['email']}
    valid_user = Register.get_email(email_data)
    if not valid_user:
        flash('invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(valid_user.password, request.form['password']):
        flash('invalid Email/Password')
        return redirect('/')
    session['user_id'] = valid_user.id
    return redirect('/user')



@app.route('/user')
def user():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('user.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')