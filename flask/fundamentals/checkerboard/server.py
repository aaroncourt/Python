from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def eight_by_8():
    return render_template('index.html', ht_num = int(8), wd_num = int(8))

@app.route('/<int:wd_num>')
def eight_by_4(wd_num):
    print(type(wd_num))
    return render_template('index.html', ht_num = int(8), wd_num = int(wd_num))

@app.route('/<int:wd_num>/<int:ht_num>')
def var_board(wd_num, ht_num):
    return render_template('index.html', wd_num = int(wd_num), ht_num = int(ht_num))

@app.route('/<int:wd_num>/<int:ht_num>/<string:color1>/<string:color2>')
def var_color_board(wd_num, ht_num, color1, color2):
    return render_template('index.html', wd_num = int(wd_num), ht_num = int(ht_num), color1 = color1, color2 = color2)

if __name__=='__main__':
    app.run(debug=True)