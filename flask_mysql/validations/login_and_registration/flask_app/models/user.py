from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import app
from flask import flash, redirect, session
import re

from flask_app.config.mysqlconnection import MySQLConnection


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def add_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(user_email)s, %(hash)s);'
        return MySQLConnection('login_and_registration').query_db(query, data)

    @staticmethod
    def validate_response(response):
        is_valid = True
        query = "SELECT email FROM users;"
        results = MySQLConnection('login_and_registration').query_db(query)

        if not str.isalpha(response['first_name']):
            flash('Please enter a name that contains only letters.', 'registration')
            is_valid = False
        elif len(response['first_name']) < 2:
            flash('Please enter a name that is at least two characters in length.', 'registration')
            is_valid = False
        
        if not str.isalpha(response['last_name']):
            is_valid = False
            flash('Please enter a name that contains only letters.', 'registration')
        elif len(response['last_name']) < 2:
            is_valid = False
            flash('Please enter a name that is at least two characters in length.', 'registration')

        if len(response['user_email']) < 1:
            flash('Please enter an email address.', 'registration')
            is_valid = False
        elif not EMAIL_REGEX.match(response['user_email']): 
            flash('Invalid email address format.', 'registration')
            is_valid = False
        for email in results:
            print(results)
            print(response['user_email'])
            if response['user_email'] == email['email']:
                flash('Email already in use.', 'registration')
                is_valid = False
                break

        if len(response['user_password']) < 8:
            flash('Please enter a password that is at least 8 characters.', 'registration')
            is_valid = False

        if not response['user_password'] == response['confirm_pass']:
            flash('Your password entries do not match.', 'registration')
            is_valid = False
        
        return is_valid
    
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = MySQLConnection('login_and_registration').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_login(login):
        is_valid = True
        if len(login['user_email']) < 1:
            flash('Invalid Email/Password', 'login')
            is_valid = False 

        if len(login['user_password']) < 1:
            flash('Invalid Email/Password', 'login')
            is_valid = False

        return is_valid
