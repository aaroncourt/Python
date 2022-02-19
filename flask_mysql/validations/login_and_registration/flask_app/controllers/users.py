from ast import dump
from flask import redirect,render_template,request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new', methods = ['POST'])
def new_user():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['user_email'] = request.form['user_email']
    
    if not User.validate_response(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['user_password'])

    data = {
        'hash': pw_hash,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'user_email': request.form['user_email'],
        'user_password': request.form['user_password'],
    }

    user_id = User.add_user(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['user_email'] = request.form['user_email']
    return redirect ('/success')

@app.route('/login', methods = ['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')

    data = {'email': request.form['user_email']}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['user_password']):
        flash('Invalid Email/Password', 'login')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name

    return redirect('/success')

@app.route('/success')
def success():
    if session.get('user_id') == None:
        return redirect('/')

    return render_template('success.html')

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect('/')