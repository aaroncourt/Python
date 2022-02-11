from flask import Flask,redirect,url_for,render_template,request,session

app=Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    # print(request.form)

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    return redirect('/result.html')

@app.route('/result', methods=['GET','POST'],)
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    results = [
        session['name'],
        session['location'],
        session['language'],
        session['comment'],
    ]
    
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(port=5000,debug=True)