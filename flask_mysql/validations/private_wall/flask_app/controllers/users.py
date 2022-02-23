from flask import redirect, render_template,request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.models.message import Message

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new', methods = ['POST'])
def new_user():
    if not User.validate_response(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['user_password'])

    data = {
        'hash': pw_hash,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'user_email': request.form['user_email'],
    }

    user_id = User.add_user(data)

    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['user_email'] = request.form['user_email']

    return redirect ('/wall')

@app.route('/login', methods = ['POST'])
def login():
    if not User.validate_login(request.form):
        print(User.validate_login(request.form))
        return redirect('/')

    data = {'email': request.form['user_email']}

    user_in_db = User.get_by_email(data)
    print(user_in_db)

    if not user_in_db:
        flash('Invalid Email/Password', 'login')
        print('Email not validated')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['user_password']):
        print(bcrypt.check_password_hash(user_in_db.password, request.form['user_password']))
        flash('Invalid Email/Password', 'login')
        print('Password not validated')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name

    return redirect('/wall')

@app.route('/wall')
def wall():
    if session.get('user_id') == None:
        return redirect('/')

    data = {
        'user_id' : session['user_id']
    }
    message_list = Message.get_messages(data)
    
    num_of_messages = 0
    
    for message in message_list:
        num_of_messages += 1

    num_sent = Message.get_sent_msgs(data)

    user_list = User.get_all_users()

    webpage_data = {
        'message_list' : message_list,
        'num_of_messages' : num_of_messages,
        'total_sent' : num_sent,
        'user_list' : user_list,
    }

    print(webpage_data)
    return render_template('wall.html', webpage_data=webpage_data)

@app.route('/send-message', methods = ['GET', 'POST'])
def new_messages():
    if session.get('user_id') == None:
        return redirect('/')

    if len(request.form['message']) < 5:
        flash('The message must be at least 5 characters long.', 'messages')
        return redirect('/wall')

    if request.form['recipient_id'] == 'select':
        flash('Please select a recipient.', 'messages')
        return redirect('/wall')


    data = {
        'creator_id' : session['user_id'],
        'message' : request.form['message'],
        'recipient_id' : request.form['recipient_id']
    }

    Message.new_message(data)
    flash('Your message has been sent', 'messages')
    return redirect('/wall')

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if session.get('user_id') == None:
        return redirect('/')

    print(request.form)

    data = {
        'message_id' : request.form['delete_button']
    }

    Message.delete_message(data)
    flash('The message has been deleted', 'delete')

    return redirect('/wall')

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect('/')