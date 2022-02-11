from flask import Flask,redirect,url_for,render_template,request
from add_user import Add_user
from get_users import Get_users

app=Flask(__name__)

@app.route('/', methods=['GET'])
def read():
    users = Get_users.get_user()
    return render_template('read.html', users = users )

@app.route('/create', methods=['GET'])
def add():
    return render_template('create.html')

@app.route('/submit', methods=['POST'])
def submit():

    data = {
        'f_name': request.form['f_name'],
        'l_name': request.form['l_name'],
        'user_email': request.form['user_email']
    }

    Add_user.add_user(data)

    return redirect('/')

if __name__ == '__main__':
    app.run(port=5000,debug=True)