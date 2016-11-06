from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/survey', methods=['POST'])
def submit_survey():
    print " stuff happened"
    name = request.form['fullName']
    dojo = request.form['dojoLocation']
    favoriteLanguage = request.form['favoriteLanguage']
    comments = request.form['comments']
    return render_template("surveyResults.html", name=name, dojo=dojo, favoriteLanguage=favoriteLanguage, comments=comments)
app.run(debug=True)
