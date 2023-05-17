from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Register:
    DB = 'registrations_schema'
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']


    @classmethod
    def create_user(cls, data):
        query = """
        insert into registrations (first_name, last_name, email, password)
        values (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result


    @classmethod
    def get_email(cls, data):
        query = """
        select * from registrations
        where email = %(email)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])




    @staticmethod
    def validate_registration(newUser):
        is_valid = True
        if len(newUser['first_name']) < 1:
            flash("First Name is required.")
            is_valid = False
        if len(newUser['last_name']) < 1:
            flash("Last Name is required.")
            is_valid = False
        if len(newUser['email']) < 1:
            flash("Email is required.")
            is_valid = False
        if not EMAIL_REGEX.match(newUser['email']):
            flash("Invalid Email.")
            is_valid = False
        if len(newUser['password']) < 1:
            flash("Password is required.")
            is_valid = False
        if len(newUser['password_confirm']) < 1:
            flash("Confirm Password is required.")
            is_valid = False
        return is_valid