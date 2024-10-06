from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from modules.sql_connection import Sql
from modules.exception import LoginError
from modules.exception import EmptyField

class LoginScreen(MDScreen):
    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")

class KioscoApp(MDApp):
    def build(self):
        return Builder.load_file('login.kv')

    def login(self, username, password):

        try:
            print(Sql.login(username, password))
        except LoginError:
            print("Oh no!")
        except EmptyField:
            print("Fill field")

    def work(self):
        print("Yes, this work")

    def nextSlide(self, screen:str):
        """Change to your screen"""
        self.root.clear_widgets()
        otherScreen = Builder.load_file(f'{screen}.kv')
        self.root.add_widget(otherScreen)

if __name__ == '__main__':
    KioscoApp().run()
