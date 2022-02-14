from flask_app.config.mysqlconnection import MySQLConnection

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * from dojos;'
        all_dojos = MySQLConnection('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in all_dojos:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = 'SELECT * FROM ninjas WHERE dojo_id = %(id)s;'
        results = MySQLConnection('dojos_and_ninjas').query_db(query, data)
        return results
    
    @classmethod
    def get_dojo_info(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = MySQLConnection('dojos_and_ninjas').query_db(query, data)
        return results
        
    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(dojo_name)s);'
        return MySQLConnection('dojos_and_ninjas').query_db(query,data)

