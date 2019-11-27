from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from app.forms import AddVisitForm
from app import app

from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Newssigmabob111!'
app.config['MYSQL_DATABASE_DB'] = 'projectDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
conn = mysql.connect()

@app.route('/index')
def index():
    buttons = {'add_visit':'add visit', 
    'add_interview':'add interview', 
    'lookup_visit':'lookup visit',
    'other':'other'}
    
    return render_template('index.html', buttons=buttons)
# buttons.add_visit = 'add visit'
#buttons.key -> value

@app.route('/add_visit', methods=['GET', 'POST'])
def add_visit():
    form = AddVisitForm()
    cursor = conn.cursor()
    if form.validate_on_submit():
        visitId = form.visit_ID.data
        patientId = form.patient_ID.data

        return 'Submitted values: \n Visit ID : {} \n Patient ID : {}'.format(visitId, patientId)
    cursor.close()
    return render_template('add_visit.html', form = form)


conn.close()