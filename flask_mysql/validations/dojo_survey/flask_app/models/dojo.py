from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Response:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.location = db_data['location']
        self.language = db_data['language']
        self.comment = db_data['comment']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);'
        return MySQLConnection('dojo_survey_schema').query_db(query,data)

    @staticmethod
    def validate_response(response):
        is_valid = True
        if response['name'] == '':
            flash('Please enter a name.')
            is_valid = False
        if response['location'] == 'default':
            flash('Please choose a location.')
            is_valid = False
        if response['language'] == 'default':
            flash('Please choose a language.')
            is_valid = False
        if response['comment'] == '':
            flash('Please enter a comment.')
            is_valid = False
        return is_valid 