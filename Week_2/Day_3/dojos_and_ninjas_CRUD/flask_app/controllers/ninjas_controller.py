from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.ninjas import Ninja



@app.route('/ninjas')
def ninjas_home():
    return render_template ('ninjas.html')