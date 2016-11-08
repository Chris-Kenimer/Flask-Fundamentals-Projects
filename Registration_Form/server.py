from flask import Flask, render_template, session, redirect, request, url_for, flash
import random
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'[A-Z0-9]')
app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def validate():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    if (request.form['first_name'].isalpha()) and (request.form['last_name'].isalpha()):
        if len(request.form['first_name']) < 1:
            flash('Please enter your first name')
        if len(request.form['last_name']) < 1:
            flash('Please enter your last name')
    else:
        flash('Your name must only include letters')
    if request.form['password'] != request.form['confirm-password']:
        flash('Passwords do not match')
    elif len(request.form['password']) < 8:
        flash('Passwords must be at least 8 characters')
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash('Passwords must include at least 1 Capital Letter and 1 Number')
    elif not EMAIL_REGEX.match(request.form['email']):
            flash('Please enter a valid email')
    else:
        flash('Successfully Registered!')
    return redirect('/')
app.run(debug=True)
