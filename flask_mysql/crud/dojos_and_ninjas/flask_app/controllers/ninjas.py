from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/ninjas/new', methods = ['POST'])
def create_ninja():
    data = {
        'dojo_id': request.form['dojo'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    print(data)
    Ninja.add_ninja(data)
    return redirect('/dojos')