from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
@app.route('/')
def index():
  return render_template("survey.html")
@app.route('/survey-submit', methods=['POST'])
def submit_survey():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    if len(request.form['name']) < 1:
        flash('Name can not be blank')
    if (len(request.form['comments']) > 120) or (len(request.form['comments']) < 5):
        flash('Comment must between 5 and 120 characters')
    return redirect('/')
app.run(debug=True)
