import pymysql
from pymysql import Error
import os
from modules.exception import LoginError, EmptyFieldError, PasswordIsNotEqualError
from dotenv import load_dotenv

class VarSql():
    def __init__(self):
        load_dotenv()
        self._connection = pymysql.connect(
            host="localhost",
            user=os.getenv('USER_DB'),
            password=os.getenv('PASSWORD_DB'),
            database="kiosco"
        )
        self._cursor = self._connection.cursor()

    def close_connection(self):
        try:
            self._connection.close()
        except Error:
            print("Connection is already closed")

class Sql(VarSql):

    def __init__(self):
        super().__init__()

    def login(self, username: str, password: str):
        """Verificar las credenciales del usuario"""

        if username == '' or password == '' or username is None or password is None:
            raise EmptyFieldError("Please fill all of fields")

        result: tuple
        column_list:tuple = ("phone", "email", "dui")

        for value in column_list:
            self._cursor.execute(f"SELECT ID FROM user WHERE {value} = %(username)s AND password = %(password)s", {'username': username, 'password': password})
            result = self._cursor.fetchone()

            # If this find the user
            if result is not None:
                self.close_connection()
                return result[0]
            
        for value in column_list:
            self._cursor.execute(f"SELECT ID FROM doctor WHERE {value} = %(username)s AND password = %(password)s", {'username': username, 'password': password})
            result = self._cursor.fetchone()

            if result is not None:
                self.close_connection()
                return result[0]

        # If this don't find the user
        self.close_connection()
        raise LoginError("Invalid credentials for username field.")

    def register_user(self, dui: str, phone: int, email: str, address: str, fullname: str, password: str, password_repeat:str, borndate: str):
        """Register a new user"""

        if password != password_repeat:
            raise PasswordIsNotEqualError("The password must be the same.")

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
                raise EmptyFieldError(f"Please fill {key}")

        sql = """
        INSERT INTO user (dui, phone, email, address, fullname, password, borndate) 
        VALUES (%(dui)s, %(phone)s, %(email)s, %(address)s, %(fullname)s, %(password)s, %(borndate)s)
        """
        
        self._cursor.execute(sql, user)
        self._connection.commit()

        self.close_connection()

    def register_doctor(self, dui:str, phone:int, email:str, fullname:str, vigilance:str, password:str, password_repeat:str):
        """Register a new Doctor"""

        if password != password_repeat:
            raise PasswordIsNotEqualError("The password must be the same.")
        
        user:dict = {
            "dui": dui,
            "phone": phone,
            "email": email,
            "fullname": fullname,
            "vigilance": vigilance,
            "password": password
        }

        for key, value in user.items():
            if value == "" or value is None:
                raise EmptyFieldError(f"Please fill {key}")
            
        sql = """
        INSERT INTO doctor (dui, phone, email, fullname, vigilance, password) 
        VALUES (%(dui)s, %(phone)s, %(email)s, %(fullname)s, %(vigilance)s, %(password)s)
        """

        self._cursor.execute(sql, user)
        self._connection.commit()

        self.close_connection()