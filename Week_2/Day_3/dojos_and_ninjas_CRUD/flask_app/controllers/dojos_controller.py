from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojos import Dojo


@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos_home():
    all_dojos = Dojo.show_dojo()
    return render_template ('dojos.html', all_dojos = all_dojos)

@app.route('/create', methods = ['post'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')