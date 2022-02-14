from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def from_root():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos = dojos)

@app.route('/new_dojo', methods = ['POST'])
def new_dojo():
    
    data = {
        'dojo_name': request.form['dojo_name']
    }

    Dojo.add_dojo(data)
    return redirect('dojos')

@app.route('/dojos/<int:id_num>')
def one_dojo(id_num):
    
    data = {
        'id' : id_num
    }

    ninjas = Dojo.get_one_dojo(data)
    dojo_info = Dojo.get_dojo_info(data)
    return render_template('dojo_profile.html', ninjas = ninjas, dojo_info = dojo_info)

