from flask_app import app
from flask import redirect,render_template,request, session
from flask_app.models.dojo import Response

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if not Response.validate_response(request.form):
        return redirect('/')

    Response.add_dojo(request.form)
    return redirect('/result')

@app.route('/result', methods=['GET'],)
def result():

    results = [
        session['name'],
        session['location'],
        session['language'],
        session['comment'],
    ]    
    return render_template('result.html', results=results)