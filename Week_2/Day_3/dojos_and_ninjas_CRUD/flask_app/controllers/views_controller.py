from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/view/<int:id>')
def ninjas_home():
    return render_template ('view.html')