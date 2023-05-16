from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []


    @classmethod
    def create_dojo(cls,data):
        query = """
        insert into dojos(name)
        values(%(name)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    

    @classmethod
    def show_dojo(cls):
        query = """
        select * from dojos;
        """

        result = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos
    

    @classmethod
    def one_dojo(cls, data):
        query = """
        select * from dojos
        join ninjas on ninjas.dojos_id = dojos.id
        where dojos.id = %(id)s
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        one_dojo = cls(result[0])
        for row in result:
            ninja_data = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at'],
                'dojos_id' : row['dojos_id']
            }
            one_dojo.all_ninjas.append(ninjas.Ninja(ninja_data))

        return one_dojo