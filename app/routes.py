from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from app.forms import AddVisitForm, AddInterviewForm, AddInitialInterviewForm, AddFollowupInterviewForm
from app import app

from flaskext.mysql import MySQL

from config import Config
import os

import datetime

mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aaa123123123'
app.config['MYSQL_DATABASE_DB'] = 'projectDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

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

        # sql = '''INSERT INTO Patient(Fie)


        
        return redirect('/followup_interview')

    return render_template('init_interview.html', form = form, buttons = buttons, data = data)

# @app.route('/test', methods = ['GET', 'POST'])
# def test():
#     form = AddInterviewForm()
#     buttons = {"save":"save"}
#     if form.validate_on_submit():
#         return "success"
#     return render_template('test.html', form = form, )


@app.route('/followup_interview')
def followup_interview():
    buttons = {
        'save':'Save'
    }
    form = AddFollowupInterviewForm()

    return render_template('followup_interview.html', form = form, buttons = buttons)


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

