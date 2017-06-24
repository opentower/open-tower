from flask import Flask, render_template
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template

app = Flask(__name__)

Mobility(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/credits')
def home():
    return render_template('credits.html')
