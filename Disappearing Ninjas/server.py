from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'TonsOfVisitsAndLotsOfFun'
@app.route('/')
def index():
    return render_template('index.html', show='none')
@app.route('/ninja')
def ninja():
    return render_template('index.html', show='turtles')
@app.route('/ninja/<color>')
def ninja_color(color):
    if color == 'blue':
        selection = 'blue'
    elif color == 'orange':
        selection = 'orange'
    elif color == 'purple':
        selection = 'purple'
    elif color == 'red':
        selection = 'red'
    else:
        selection = 'april'
    return render_template('index.html', show=selection)
app.run(debug=True)
