from http.client import responses
from flask import redirect, render_template,request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if session.get('user_id') == None:
        return redirect('/')

    data = {
        'user_id' : session['user_id']
    }

    recipes = Recipe.get_recipes()

    return render_template('dashboard.html', recipes = recipes)

@app.route('/recipe/<int:recipe_id>')
def read_recipe(recipe_id):
    if session.get('user_id') == None:
        return redirect('/')

    data = {
        'recipe_id' : recipe_id,
    }
    recipe_info = Recipe.get_recipe(data)

    return render_template('read.html', recipe_info = recipe_info)

@app.route('/recipe/new')
def new_recipe():
    if session.get('user_id') == None:
        return redirect('/')

    return render_template('add.html')

@app.route('/recipe/create', methods = ['POST'])
def create_recipe():
    if session.get('user_id') == None:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/new')

    data = {
    'name' : request.form['name'],
    'description' : request.form['description'],
    'instructions' : request.form['instructions'],
    'under_30' : request.form['under_30'],
    'date_made' : request.form['date_made'],
    }

    Recipe.add_recipe(data)

    return redirect('/dashboard')

@app.route('/recipe/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if session.get('user_id') == None:
        return redirect('/')

    data = {
        'recipe_id' : recipe_id,
    }
    recipe_info = Recipe.get_recipe(data)

    return render_template('edit.html', recipe_info = recipe_info)

@app.route('/recipe/edit/submit', methods = ['POST'])
def submit_edit():
    if session.get('user_id') == None:
        return redirect('/')

    recipe_id = request.form['recipe_id']

    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/edit/'+recipe_id)

    data = {
    'recipe_id' : request.form['recipe_id'],
    'name' : request.form['name'],
    'description' : request.form['description'],
    'instructions' : request.form['instructions'],
    'under_30' : request.form['under_30'],
    'date_made' : request.form['date_made'],
    'name' : request.form['name'],
    }

    Recipe.update_recipe(data)

    return redirect('/dashboard')

@app.route('/recipe/delete/<int:recipe_id>', methods = ['GET','POST']
    )
def remove_recipe(recipe_id):
    if session.get('user_id') == None:
        return redirect('/')

    data = {
        'recipe_id' : recipe_id,
    }

    Recipe.delete_recipe(data)

    return redirect('/dashboard')

