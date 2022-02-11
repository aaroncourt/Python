from mysqlconnection import MySQLConnection

class Get_user:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_user(cls, data):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        results =  MySQLConnection('users_schema').query_db(query, data)
        print(results)
        return results