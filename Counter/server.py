from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
@app.route('/')
def index():
    if session.get('counter'):
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html')
@app.route('/ninjas')
def ninjas():
    session['counter'] += 1
    return redirect('/')
@app.route('/hackers')
def hackers():
    session['counter'] = -1
    return redirect('/')
app.run(debug=True)
