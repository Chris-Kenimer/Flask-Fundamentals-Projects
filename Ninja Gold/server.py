from flask import Flask, render_template, session, redirect, request, url_for
import random
import datetime
app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
log = []
value = 0
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.datetime.now()
    global value
    if request.form['gold'] == 'farm':
        gold = random.randrange(10,21)
        value += gold
        log.insert(0,{'farm':[gold, now]})
    elif request.form['gold'] == 'cave':
        gold = random.randrange(5,11)
        value += gold
        log.insert(0,{'cave':[gold, now]})
    elif request.form['gold'] == 'house':
        gold = random.randrange(2,5)
        value += gold
        log.insert(0,{'house':[gold, now]})
    elif request.form['gold'] == 'casino':
        gold = random.randrange(-51,51)
        value += gold
        log.insert(0,{'casino':[gold, now]})
    session['value'] = value
    session['log'] = log
    return redirect('/')
@app.route('/reset')
def reset():
    session['value'] = 0
    session['log'] = []
    return redirect('/')
app.run(debug=True)
