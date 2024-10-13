from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
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

class MainUserScreen(Screen):
    pass

class ManagementMedicineUserScreen(Screen):
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
        sm.add_widget(MainUserScreen(name='MainUserScreen'))
        sm.add_widget(ManagementMedicineUserScreen(name='ManagementMedicineUserScreen'))

        sm.current = 'LoginScreen'

        # You don't need this!
        # Builder.load_file('kiosco.kv')

        #self.screen_manager = Builder.load_file('kiosco.kv')
        return sm

    def login(self, username, password):
        try:
            user:tuple = self.sql.login(username=username, password=password)
            
            if user[1] == True:
                self.change_screen('MainUserScreen')
            else:
                self.change_screen('MainUserScreen') # TODO: change this to MainDoctorScreen
            
        except LoginError: self.snackDialog("¡Usuario o contraseña incorrectos!")
        except EmptyFieldError: self.snackDialog("¡Por favor llena todos los campos!")

    def register_user(self, dui:str, name:str, phone:int, email:str, address:str, borndate:str, password:str, password_repeat:str):
        try: self.sql.register_user(dui,phone,email,address,name,password,password_repeat,borndate)
        except EmptyFieldError: self.snackDialog("¡Por favor llena todos los campos!")
        except PasswordIsNotEqualError: self.snackDialog("¡La contraseña debe ser igual!")

    def register_doctor(self, dui:str, phone:int, email:str, fullname:str, vigilance:str, password:str, password_repeat:str):
        try: self.sql.register_doctor(dui,phone, email, fullname, vigilance, password, password_repeat)
        except EmptyFieldError: self.snackDialog("¡Por favor llena todos los campos!")
        except PasswordIsNotEqualError: self.snackDialog("¡La contraseña debe ser igual!")

    def snackDialog(self,text:str):
            MDSnackbar(
                MDSnackbarText(
                    text=text,
                    text_color= (0,0,0,1)
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
                background_color = (1,1,1,1), # self.theme_cls.onPrimaryContainerColor
            ).open()

    def work(self):
        print("Yes, this work")

    def change_screen(self, screen):
        self.root.current = screen

if __name__ == '__main__':
    KioscoApp().run()
