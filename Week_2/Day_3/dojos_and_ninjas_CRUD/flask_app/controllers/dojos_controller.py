from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojos import Dojo


@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos_home():
    return render_template ('dojos.html')
