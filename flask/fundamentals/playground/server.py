import numbers
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play/<int:num>/<color>')
def boxes(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
