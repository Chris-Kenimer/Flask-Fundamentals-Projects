from flask import Flask, render_template, session, redirect, request, url_for
import random
app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
@app.route('/')
def index():
    if session.get('randomNumber'):
        print session['guess']
        print session['randomNumber']
        if int(session['guess']) == session['randomNumber']:
            answer = 'True'
        elif int(session['guess']) < session['randomNumber']:
            answer = 'Too Low'
        elif int(session['guess']) > session['randomNumber']:
            answer = 'Too High'
    else:
        answer = ''
        session['randomNumber'] = random.randrange(0,101)
    return render_template('index.html', answer=answer)
@app.route('/guess', methods=['POST'])
def guess():
    random = session['randomNumber']
    session['guess'] = request.form['guess']
    return redirect('/')
@app.route('/reset')
def reset():
    session.pop('randomNumber', None)
    return redirect('/')
app.run(debug=True)
