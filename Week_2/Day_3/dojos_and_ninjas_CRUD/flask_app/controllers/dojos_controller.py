from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos_home():
    dojos = Dojo.show_dojo()
    return render_template ('dojos.html', dojos = dojos)

@app.route('/create', methods = ['post'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')



@app.route('/view/<int:id>')
def views_home(id):
    one_dojo = Dojo.one_dojo({'id' : id})
    return render_template ('view.html', one_dojo = one_dojo)