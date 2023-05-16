from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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

        result = connectToMySQL(cls.DB).query_db(query,)
        all_dojos = []
        for dojo in result:
            all_dojos.append(cls(dojo))
        return all_dojos
    
    