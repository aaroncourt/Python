from flask_app.config.mysqlconnection import MySQLConnection

class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_users(cls):
        query = 'SELECT * FROM users;'
        results =  MySQLConnection('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
        
    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        results =  MySQLConnection('users_schema').query_db(query, data)
        return results

    @classmethod
    def add_user(cls, data):
        query = 'INSERT INTO users ( first_name, last_name, email) VALUES ( %(f_name)s, %(l_name)s, %(user_email)s);'

        return MySQLConnection('users_schema').query_db(query, data)

    @classmethod
    def edit_user(cls, data):
        query = 'UPDATE users SET first_name = %(f_name)s, last_name = %(l_name)s, email = %(user_email)s WHERE id=%(id)s;'

        return MySQLConnection('users_schema').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return MySQLConnection('users_schema').query_db(query, data)