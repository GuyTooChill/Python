from mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = """
        insert into users (first_name, last_name, email)
        values(%(first_name)s, %(last_name)s, %(email)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def show_users(cls):
        query = """
        select * from users;
        """

        result = connectToMySQL(cls.DB).query_db(query)
        all_users = []
        for users in result:
            all_users.append(cls(users))
        return all_users