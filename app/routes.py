from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from app.forms import AddVisitForm
from app import app


@app.route('/index')
def index():
    buttons = {'add_visit':'add visit', 
    'add_interview':'add interview', 
    'lookup_visit':'lookup visit',
    'other':'other'}
    
    return render_template('index.html', buttons=buttons)
# buttons.add_visit = 'add visit'
#buttons.key -> value

@app.route('/add_visit')
def add_visit():
    form = AddVisitForm()
    return render_template('add_visit.html', form = form)