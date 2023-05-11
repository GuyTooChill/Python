from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.users import User

app = Flask(__name__)    

@app.route('/')         
def hello_world():
    return render_template ("read.html")


@app.route('/create')         
def hello_world():
    return render_template ("create.html")