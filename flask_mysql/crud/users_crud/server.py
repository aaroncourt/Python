from dataclasses import dataclass
from flask import Flask,redirect,url_for,render_template,request
from add_user import Add_user
from get_users import Get_users
from get_user import Get_user
from edit_one import Edit_user

app=Flask(__name__)

#redirect from root
@app.route('/', methods=['GET'])
def show_all():
    return redirect('/users')

#get all users and home page
@app.route('/users', methods=['GET'])
def read_all():
    users = Get_users.get_users()
    return render_template('read.html', users=users )

#show one user by id
@app.route('/users/<int:id_num>', methods=['GET','POST'])
def read_one(id_num):

    data = {
        'id':id_num
    }

    user_info = Get_user.get_user(data)


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

    result = Add_user.add_user(data)
    return redirect(f'/users/{result}')


#edit one user
@app.route('/users/<int:id_num>/edit')
def edit_one(id_num):
    
    data = {
        'id':id_num
    }

    user_info = Get_user.get_user(data)


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

    result = Edit_user.edit_user(data)
    print(id_num)

    return redirect(f'/users/{id_num}')

#delete one user
@app.route('/delete/<int:id_num>')
def destroy_one(id_num):

    data = {
        'id': id_num
    }
    
    Edit_user.delete_user(data)
    return redirect('/users')

if __name__ == '__main__':
    app.run(port=5000,debug=True)