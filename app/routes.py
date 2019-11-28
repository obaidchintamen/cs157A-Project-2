from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from app.forms import AddVisitForm, AddInterviewForm, AddInitialInterviewForm, AddFollowupInterviewForm
from app import app

from flaskext.mysql import MySQL

from config import Config
import os

import datetime
"""
this creates connection to the MySQL Database
"""
mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'obaid'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aaa123123123'
app.config['MYSQL_DATABASE_DB'] = 'projectDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


"""
Routes to the initial page at /index or / route

Renders index.html page

It passes buttons data to the index.html template
"""
@app.route('/')
@app.route('/index')
def index():
    buttons = {
        'add_visit':'Add Visit', 
        'add_interview':'Interview', 
        'lookup_visit':'Lookup Visit',
        'other':'Other',
        }
    return render_template('index.html', buttons = buttons)


"""
Routes to the add visit page at /add_visit route
Renders add_visit.html page

Add Visit button from index.html page also gets you to this page

This page has a form and uses the AddVisitForm() class to pass
the form fields to add_visit.html template

if the form is valid when the user submits, then a connection
is opened and a cursor is created. Then the form values are 
passed to the sql statement which is executed and committed.

user data is also queried and passed to the html template
"""
@app.route('/add_visit', methods=['GET', 'POST'])
def add_visit():
    buttons = {
        'add':'Add Visit'
    }
    form = AddVisitForm()
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor()

        visitId = form.visit_ID.data
        thc = form.thc_number.data
        # date = form.date.data
        visitNum = form.visit_num.data

        sql = '''INSERT INTO Visit (THC, Visit_Num) 
        VALUES ({},{})'''.format(thc,visitNum)
        
        cursor.execute(sql)
        conn.commit()

        sql = '''SELECT * FROM Visit 
                NATURAL JOIN Patient 
                ORDER BY Visit_ID DESC LIMIT 1'''
        cursor.execute(sql)
        x = None
        for row in cursor.fetchall():
            x = row

        data = {
            'data': "Visit ID: {}, Date: {}, THC#: {}, Patient Name: {} {}, Visit Number: {}".format(x[1], x[3], x[0], x[4], x[5], x[2])
        }

        cursor.close()
        conn.close()
        # return 'Submitted values: \n date: {}'.format(date)
        return render_template('add_interview.html', 
        form = AddInterviewForm(), 
        buttons = {'initial_followup':'Initial/Followup',
        'thi':'THI',
        'tfi':'TFI',
        'add_md':'Add MD'},
        data = data)
    
    return render_template('add_visit.html', butons = buttons, form = form)

"""
Routes to /add_interview page
Renders add_interview.html

This page has a form and uses the AddVisitForm() class to pass
the form fields to add_visit.html template

Displays information for the most recent patient at the top
"""
@app.route('/add_interview')
def add_interview():
    buttons = {
        'initial_followup':'Initial/Followup',
        'thi':'THI',
        'tfi':'TFI',
        'add_md':'Add MD'
    }
    form = AddInterviewForm()

    conn = mysql.connect()
    cursor = conn.cursor()

    sql = '''SELECT * FROM Visit 
            NATURAL JOIN Patient 
            ORDER BY Visit_ID DESC LIMIT 1'''
    cursor.execute(sql)
    
    x = None
    for row in cursor.fetchall():
        x = row

    data = {
        'data': "Visit ID: {}, Date: {}, THC#: {}, Patient Name: {} {}, Visit Number: {}".format(x[1], x[2], x[0], x[4], x[5], x[3])
    }

    cursor.close()
    conn.close()

    if form.validate_on_submit():
        return "submitted"


    return render_template('add_interview.html', form = form, buttons = buttons, data = data)

"""
Routes to /init_intervew page
Renders init_interview.html

This page has a form and uses the AddInitialInterviewForm() class to pass
the form fields to init_interview.html template

Displays information for the most recent patient at the top

Inserts Values from form : clinicNum, thcNum

redirects to /followup_interview if form submits

"""
@app.route('/init_interview', methods = ['GET', 'POST'])
def init_interview():
    buttons = {
        'save':'Save'
    }
    form = AddInitialInterviewForm()

    conn = mysql.connect()
    cursor = conn.cursor()
    sql = '''SELECT * FROM Visit 
            NATURAL JOIN Patient 
            ORDER BY Visit_ID DESC LIMIT 1'''
    cursor.execute(sql)
    
    x = None
    for row in cursor.fetchall():
        x = row

    data = {
        'data': "Visit ID: {}, Date: {}, THC#: {}, Patient Name: {} {}, Visit Number: {}".format(x[1], x[3], x[0], x[4], x[5], x[2])
    }
    cursor.close()
    conn.close()
    
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor()
    
        clinicNum = form.clinic_number.data
        thcNum = form.thc.data

        sql = '''INSERT INTO Interview (Clinic_Num,
        THC_Num) VALUE ({},{})'''.format(clinicNum,thcNum)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

        # conn = mysql.connect()
        # cursor = conn.cursor()

        # firstname = form.first_name.data
        # lastname = form.last_name.data

        # sql = '''INSERT INTO Patient(THC, First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email)


        
        return redirect('/followup_interview')

    return render_template('init_interview.html', form = form, buttons = buttons, data = data)

"""
Routes to /followup_interview page
Renders followup_interview.html

This page has a form and uses the AddFollowupInterviewForm() class to pass
the form fields to init_interview.html template

Inserts Values from form : clinicNum, thcNum

redirects to /index if form submits

"""

@app.route('/followup_interview' , methods = ['GET', 'POST'])
def followup_interview():
    buttons = {
        'save':'Save'
    }
    form = AddFollowupInterviewForm()
    # if form.validate_on_submit():
    #     return redirect('/index')
    # if request.method == "POST":
    #     return redirect('/index')
    if form.validate_on_submit():
        conn = mysql.connect()
        cursor = conn.cursor()
    
        clinicNum = form.clinic_number.data
        thcNum = form.thc.data

        sql = '''INSERT INTO Interview (Clinic_Num,
        THC_Num) VALUE ({},{})'''.format(clinicNum,thcNum)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect('/index')

    return render_template('followup_interview.html', form = form, buttons = buttons)

"""
Routes to /look_up page
Renders look_up.html

Queries all patient names and returns them
"""
@app.route('/lookup_visit')
def lookup_visit():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = '''SELECT First_Name FROM Visit 
            NATURAL JOIN Patient 
            WHERE Visit_Num = 1 
            ORDER BY THC DESC LIMIT 10 '''
    cursor.execute(sql)
    x = []
    for row in cursor.fetchall():
        x.append(row)
    data = {
        'data':x
    }
    return render_template('lookup_visit.html', data = data)

