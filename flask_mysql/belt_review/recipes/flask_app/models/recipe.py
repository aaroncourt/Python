from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import app
from flask import flash, request
import re

DATE_REGEX = re.compile(r'^20[0-2][0-9]-((0[1-9])|(1[0-2]))-(0[1-9]|[1-2][0-9]|3[0-1])$') 

class Recipe:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.under_30 = db_data['under_30']
        self.date_made = db_data['date_made']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def add_recipe(cls, data):
        query = 'INSERT INTO recipes (name, description, instructions, under_30, date_made) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date_made)s);'

        return MySQLConnection('recipes').query_db(query,data)

    @classmethod
    def get_recipes(cls):
        query = 'SELECT * FROM recipes;'
        results = MySQLConnection('recipes').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))

        return recipes

    @classmethod
    def get_recipe(cls, data):
        query = 'SELECT * FROM recipes WHERE id=%(recipe_id)s;'
        results =  MySQLConnection('recipes').query_db(query, data)


        return cls(results[0])

    @classmethod
    def update_recipe(cls, data):
        query = 'UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, date_made = %(date_made)s WHERE id = %(recipe_id)s;'

        return MySQLConnection('recipes').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(recipe_id)s;'

        return MySQLConnection('recipes').query_db(query, data)

    @staticmethod
    def validate_recipe(response):
        is_valid = True

        if len(response['name']) < 3:
            flash('Please enter a name that is at least three characters in length.', 'recipe')
            is_valid = False
        if len(response['description']) < 3:
            flash('Please enter a description that is at least three characters in length.', 'recipe')
            is_valid = False
        if len(response['instructions']) < 3:
            flash('Please enter instructions that are at least three characters in length.', 'recipe')
            is_valid = False
        if not DATE_REGEX.match(response['date_made']): 
            flash('Invalid date format.', 'recipe')
            is_valid = False

        return is_valid