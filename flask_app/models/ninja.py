from flask_app.config.mysqlconnection import connectToMySQL

db='dojo_and_ninjas_schema'

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data ['age']
        self.created_at = data["created_at"]
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query)
        ninjas= []
        for one_row in results:
            ninjas.append(cls(one_row))
        return ninjas




    @classmethod
    def create(cls, data):
        query = """
        INSERT into ninjas (first_name, last_name, age, dojo_id) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        """
        result = connectToMySQL(db).query_db(query, data)
        print(result)
        return result
