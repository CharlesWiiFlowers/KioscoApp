from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from modules.sql_connection import Sql
from modules.exception import LoginError
from modules.exception import EmptyFieldError
from modules.exception import PasswordIsNotEqualError

class LoginScreen(Screen):
    pass

class SwitchRegisterScreen(Screen):
    pass

class RegisterDoctorScreen(Screen):
    pass

class RegisterUserScreen(Screen):
    pass

class KioscoApp(MDApp):

    # Build the class
    sql = Sql()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

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
            print(self.sql.login(username=username, password=password))
        except LoginError:
            print("Oh no!")
        except EmptyFieldError:
            print("Fill field")

    def register_user(self, dui:str, name:str, phone:int, email:str, address:str, borndate:str, password:str, password_repeat:str):
        try: self.sql.register_user(dui,phone,email,address,name,password,password_repeat,borndate)
        except EmptyFieldError:
            print("Fill fields!")
        except PasswordIsNotEqualError:
            print("Password must be the same!")

    def register_doctor(self, dui:str, phone:int, email:str, fullname:str, vigilance:str, password:str, password_repeat:str):
        try: self.sql.register_doctor(dui,phone, email, fullname, vigilance, password, password_repeat)
        except EmptyFieldError:
            print("Fill fields!")
        except PasswordIsNotEqualError:
            print("Passowrd have to be the same!")

    def work(self):
        print("Yes, this work")

    def change_screen(self, screen):
        self.root.current = screen

if __name__ == '__main__':
    KioscoApp().run()
