from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = " SELECT * FROM dojos"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        print(results)
        dojos = []
        for i in results:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id where dojos.id= (%(id)s);"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
        print('A')
        for dictionary in results:
            print(dictionary)
        print('B')
        print(results[0])
        one_dojo= cls(results[0])
        print(one_dojo)
        for row in results:
            for key in row:
                print(key, "\t\t", row[key])
            ninja_data= {
                "id": row["ninjas.id"],
                "first_name":row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"],
                "dojo_id": row["dojo_id"]
            }
            one_ninja=ninja.Ninja(ninja_data)
            one_dojo.ninjas.append(one_ninja)

        return one_dojo


        


