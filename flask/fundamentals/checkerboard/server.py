from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def eight_by_8():
    return render_template('index.html', ht = 8, wd = 8)

@app.route('/<int:wd_num>')
def eight_by_4(wd_num):
    return render_template('index.html', ht = 8, wd = wd_num)

@app.route('/<int:wd_num>/<int:ht_num>')
def var_board(wd_num, ht_num):
    return render_template('index.html', wd = wd_num, ht = ht_num)

@app.route('/<int:wd_num>/<int:ht_num>/color1/color2')
def var_color_board(wd_num, ht_num, color1, color2):
    return render_template(wd = wd_num, ht = ht_num, color1 = color1, color2 = color2)

if __name__=='_main__':
    app.run(debug=True)