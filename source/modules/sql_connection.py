import pymysql
from pymysql import Error
import os
from modules.exception import LoginError
from modules.exception import EmptyField
from dotenv import load_dotenv

class VarSql():
    load_dotenv()
    connection = pymysql.connect(
        host="localhost",
        user=os.getenv('USER_DB'),
        password=os.getenv('PASSWORD_DB'),
        database="kiosco"
    )
    cursor = connection.cursor()

class Sql(VarSql):
    def login(username:str, password:str):

        if username == '' or password == '' or username == None or password == None:
            raise EmptyField("Please fill all of fields")

        result:tuple
        column_list = ("phone", "email", "dui")

        for key in column_list:
            Sql.cursor.execute(f"SELECT ID FROM user WHERE {key} = %(username)s AND password = %(password)s", {'username': username, 'password': password})
            result = Sql.cursor.fetchone()

            # Only return if result isn't None
            if result is not None:
                try: Sql.connection.close()
                except Error: print("Connection is already closely")
                finally: return result[0]

        # If result is None
        try: Sql.connection.close()
        except Error: print("Connection is already closely")
        finally: raise LoginError("Invalid credentials for username field")
    

    # TO DO, this works?
    def register_user(dui:str, phone:int, email:str, address:str, fullname:str, password:str, borndate:str):
        """Register a new user"""
        try:
            user:dict = {"dui": dui, "phone": phone, "email": email, "address": address, "fullname": fullname, "password": password, "borndate": borndate}

            for key, value in user:
                if value == "" or value == None:
                    raise EmptyField(f"Please fill {key}")
                
            sql = "INSERT INTO user (dui, phone, email, address, fullname, password, borndate) VALUES (%(dui), %(phone)s, %(email)s, %(address)s, %(fullname)s, %(password)s, %(borndate)s)"
            values = {key:value for key,value in user}

            Sql.cursor.execute(sql, values)
            Sql.connection.commit()
        finally:
            try: Sql.connection.close();
            except Error: print("Connection is already closed")


