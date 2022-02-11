from mysqlconnection import connectToMySQL

class Add_user:
    def __init__(self, form_data):
        self.f_name = form_data['f_name']
        self.l_name = form_data['l_name']
        self.user_email = form_data['user_email']
        
    @classmethod
    def add_user(cls, data):
        query = 'INSERT INTO users ( first_name, last_name, email) VALUES ( %(f_name)s, %(l_name)s, %(user_email)s);'

        return connectToMySQL('users_schema').query_db(query, data)