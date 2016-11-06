from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("survey.html")
@app.route('/survey-submit', methods=['POST'])
def submit_survey():
    return render_template("survey_results.html", results=request.form)
app.run(debug=True)
