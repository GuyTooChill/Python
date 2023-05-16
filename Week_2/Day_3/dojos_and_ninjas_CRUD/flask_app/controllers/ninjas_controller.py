from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo



@app.route('/ninjas')
def ninjas_home():
    dojos = Dojo.show_dojo()
    return render_template ('ninjas.html', dojos = dojos)


@app.route('/create_ninja', methods = ['post'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/')