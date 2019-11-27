from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from app.forms import AddVisitForm
from app.forms import AddInterviewForm
from app.forms import AddInitialInterviewForm
from app import app

@app.route('/index')
def index():
    buttons = {
        'add_visit':'Add Visit', 
        'add_interview':'Add Interview', 
        'lookup_visit':'Lookup Visit',
        'other':'Other',
        }
    
    return render_template('index.html', buttons = buttons)
# buttons.add_visit = 'add visit'
#buttons.key -> value

@app.route('/add_visit')
def add_visit():
    buttons = {
        'add':'Add Visit'
    }
    form = AddVisitForm()
    return render_template('add_visit.html', buttons = buttons, form = form)

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
    if form.validate_on_submit():
        flash('Initial Interview Form submitted!')
        return redirect(url_for('index'))
    return render_template('init_interview.html', form = form)