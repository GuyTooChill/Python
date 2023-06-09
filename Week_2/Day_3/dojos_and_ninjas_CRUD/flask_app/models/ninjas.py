from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojos_id']

    @classmethod
    def create_ninja(cls, data):
        query = """
        insert into ninjas (first_name, last_name, age, dojos_id)
        values(%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
