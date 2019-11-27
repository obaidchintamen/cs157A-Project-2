from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from app.forms import AddVisitForm
from app.forms import AddInterviewForm
from app.forms import AddInitialInterviewForm
from app.forms import AddFollowupInterviewForm
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
    form = AddVisitForm()
    return render_template('add_visit.html', form = form)

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

@app.route('/init_interview')
def init_interview():
    buttons = {
        'save':'Save'
    }
    form = AddInitialInterviewForm()
    return render_template('init_interview.html', form = form, buttons = buttons)

@app.route('/followup_interview')
def followup_interview():
    buttons = {
        'save':'Save'
    }
    form = AddFollowupInterviewForm()
    return render_template('followup_interview.html', form = form, buttons = buttons)