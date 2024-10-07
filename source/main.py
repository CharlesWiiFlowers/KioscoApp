from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from modules.sql_connection import Sql
from modules.exception import LoginError
from modules.exception import EmptyField

class LoginScreen(Screen):
    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")

    def work(self):
        print("wtf this work?")

class SwitchRegisterScreen(Screen):
    pass

class RegisterDoctorScreen(Screen):
    def work(self):
        print("OMG THIS WORK!")

class RegisterUserScreen(Screen):
    pass

class KioscoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='LoginScreen'))
        sm.add_widget(SwitchRegisterScreen(name='SwitchRegisterScreen'))
        sm.add_widget(RegisterDoctorScreen(name='RegisterDoctorScreen'))
        sm.add_widget(RegisterUserScreen(name='RegisterUserScreen'))

        sm.current = 'LoginScreen'

        Builder.load_file('kiosco.kv')

        #self.screen_manager = Builder.load_file('kiosco.kv')
        return sm

    def login(self, username, password):
        try:
            print(Sql.login(username, password))
        except LoginError:
            print("Oh no!")
        except EmptyField:
            print("Fill field")

    def work(self):
        print("Yes, this work")

    def change_screen(self, screen):
        self.root.current = screen

if __name__ == '__main__':
    KioscoApp().run()
