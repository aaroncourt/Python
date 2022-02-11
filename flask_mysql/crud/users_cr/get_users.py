from mysqlconnection import MySQLConnection

class Get_users:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_user(cls):
        query = 'SELECT * FROM users'
        results =  MySQLConnection('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        print(users)
        return users