from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")

class KioscoApp(MDApp):
    def build(self):
        return Builder.load_file('login.kv')

    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")

if __name__ == '__main__':
    KioscoApp().run()
