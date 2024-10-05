import pymysql
import os
from modules.exception import LoginError
from dotenv import load_dotenv

class Sql():

    load_dotenv()
    connection = pymysql.connect(
        host="localhost",
        user=os.getenv('USER_DB'),
        password=os.getenv('PASSWORD_DB'),
        database="kiosco"
    )
    cursor = connection.cursor()

    def login(username:str, password:str):

        result:tuple
        column_list = ("phone", "email", "dui")

        for key in column_list:
            Sql.cursor.execute(f"SELECT ID FROM user WHERE {key} = {username} AND password = {password}")
            result = Sql.cursor.fetchone()

        if result is not None:
            id = result[0]
            return id
        else:
            raise LoginError("Invalid credentials for username field")