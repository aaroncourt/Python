from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total_fruit = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple']) + int(request.form['blackberry'])
    customer_name = request.form['first_name'] + ' ' + request.form['last_name']
    print(request.form)
    print(f'Charging {customer_name} for {total_fruit} fruit(s)')
    return render_template ("checkout.html", total_fruits = total_fruit) 

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    