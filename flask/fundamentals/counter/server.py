from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = '\x92\xb6?`8C  \xaf\x7f^\xb1\xe1\x8d\x12ta\xda'

# session['counter'] = 0

@app.route('/', methods = ['get', 'post'])
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter = session['counter'])

@app.route('/counter', methods = ['post'])
def counter():
    session['counter'] +=1
    return redirect('/')

@app.route('/destroy_session', methods = ['post'])
def destroy():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)