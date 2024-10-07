import pymysql
from pymysql import Error
import os
from modules.exception import LoginError, EmptyField
from dotenv import load_dotenv

class VarSql():
    def __init__(self):
        load_dotenv()
        self.__connection = pymysql.connect(
            host="localhost",
            user=os.getenv('USER_DB'),
            password=os.getenv('PASSWORD_DB'),
            database="kiosco"
        )
        self._cursor = self.__connection.cursor()

    def close_connection(self):
        try:
            self.__connection.close()
        except Error:
            print("Connection is already closed")

class Sql(VarSql):

    def __init__(self):
        super().__init__()

    def login(self, username: str, password: str):
        """Verificar las credenciales del usuario"""

        if username == '' or password == '' or username is None or password is None:
            raise EmptyField("Please fill all of fields")

        result: tuple
        column_list = ("phone", "email", "dui")

        for key in column_list:
            self._cursor.execute(f"SELECT ID FROM user WHERE {key} = %(username)s AND password = %(password)s", {'username': username, 'password': password})
            result = self._cursor.fetchone()

            # If this find the user
            if result is not None:
                self.close_connection()
                return result[0]

        # If this don't find the user
        self.close_connection()
        raise LoginError("Invalid credentials for username field")

    def register_user(self, dui: str, phone: int, email: str, address: str, fullname: str, password: str, borndate: str):
        """Register a new user"""
        user: dict = {
            "dui": dui, 
            "phone": phone, 
            "email": email, 
            "address": address, 
            "fullname": fullname, 
            "password": password, 
            "borndate": borndate
        }

        for key, value in user.items():
            if value == "" or value is None:
                raise EmptyField(f"Please fill {key}")

        sql = """
        INSERT INTO user (dui, phone, email, address, fullname, password, borndate) 
        VALUES (%(dui)s, %(phone)s, %(email)s, %(address)s, %(fullname)s, %(password)s, %(borndate)s)
        """
        
        self._cursor.execute(sql, user)
        self.__connection.commit()

        self.close_connection()
