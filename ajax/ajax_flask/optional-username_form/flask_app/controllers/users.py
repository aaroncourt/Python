from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

#redirect from root
@app.route('/', methods=['GET'])
def show_all():
    return redirect('/users')

#get all users and home page
@app.route('/users', methods=['GET'])
def read_all():
    users = User.get_users()
    return render_template('read.html', users=users )

#show one user by id
@app.route('/users/<int:id_num>', methods=['GET','POST'])
def read_one(id_num):

    data = {
        'id':id_num
    }

    user_info = User.get_user(data)


    return render_template('read_one.html', user_info=user_info)

#form for new user
@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template('create.html')

#add one user to DB after form submitted
@app.route('/submit', methods=['POST'])
def submit():

    data = {
        'f_name': request.form['f_name'],
        'l_name': request.form['l_name'],
        'user_email': request.form['user_email']
    }

    result = User.add_user(data)
    return redirect(f'/users/{result}')


#edit one user
@app.route('/users/<int:id_num>/edit')
def edit_one(id_num):
    
    data = {
        'id':id_num
    }

    user_info = User.get_user(data)


    return render_template('edit_one.html', user_info=user_info)

#edit user in DB after submitted form
@app.route('/edit/<int:id_num>', methods=['POST'])
def edit(id_num):

    data = {
        'id': id_num,
        'f_name': request.form['f_name'],
        'l_name': request.form['l_name'],
        'user_email': request.form['user_email']
    }

    result = User.edit_user(data)
    print(id_num)

    return redirect(f'/users/{id_num}')

#delete one user
@app.route('/delete/<int:id_num>')
def destroy_one(id_num):

    data = {
        'id': id_num
    }
    
    User.delete_user(data)
    return redirect('/users')