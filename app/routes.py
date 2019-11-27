from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from app.forms import AddVisitForm, AddInterviewForm, AddInitialInterviewForm, AddFollowupInterviewForm
from app import app

from flaskext.mysql import MySQL
from config import Config
import os

mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Siri4634!'
app.config['MYSQL_DATABASE_DB'] = 'projectDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

conn = mysql.connect()

@app.route('/index')
def index():
    buttons = {
        'add_visit':'Add Visit', 
        'add_interview':'Add Interview', 
        'lookup_visit':'Lookup Visit',
        'other':'Other',
        }
    return render_template('index.html', buttons = buttons)


@app.route('/add_visit', methods=['GET', 'POST'])
def add_visit():
    buttons = {
        'add':'Add Visit'
    }
    form = AddVisitForm()
    cursor = conn.cursor()
    if form.validate_on_submit():
        visitId = form.visit_ID.data
        patientId = form.patient_ID.data

        return 'Submitted values: \n Visit ID : {} \n Patient ID : {}'.format(visitId, patientId)
    cursor.close()
    return render_template('add_visit.html', butons = buttons, form = form)


@app.route('/add_interview')
def add_interview():
    buttons = {
        'initial_followup':'Initial/Followup',
        'thi':'THI',
        'tfi':'TFI',
        'add_md':'Add MD'
    }
    form = AddInterviewForm()
    return render_template('add_interview.html', form = form, buttons = buttons)

@app.route('/init_interview', methods = ['GET', 'POST'])
def init_interview():
    form = AddInitialInterviewForm()
    return render_template('init_interview.html', form = form, buttons = buttons)

@app.route('/followup_interview')
def followup_interview():
    buttons = {
        'save':'Save'
    }
    form = AddFollowupInterviewForm()
    return render_template('followup_interview.html', form = form, buttons = buttons)



conn.close()
