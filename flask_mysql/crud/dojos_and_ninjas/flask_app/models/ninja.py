from flask_app.config.mysqlconnection import MySQLConnection

class Ninja:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def get_all_ninjas_by_dojo(cls, data):
        query = 'SELECT * from ninjas WHERE dojo_id = %(id)s;'
        results = MySQLConnection('dojos_and_ninjas').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one_ninja(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s;'
        results = MySQLConnection('dojos_and_ninjas').query_db(query, data)
        return results
        
    @classmethod
    def add_ninja(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return MySQLConnection('dojos_and_ninjas').query_db(query,data)

