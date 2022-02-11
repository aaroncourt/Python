from mysqlconnection import connectToMySQL

class Edit_user:
    def __init__(self, form_data):
        self.f_name = form_data['f_name']
        self.l_name = form_data['l_name']
        self.user_email = form_data['user_email']
        
    @classmethod
    def edit_user(cls, data):
        query = 'UPDATE users SET first_name = %(f_name)s, last_name = %(l_name)s, email = %(user_email)s WHERE id=%(id)s;'

        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        return connectToMySQL('users_schema').query_db(query, data)