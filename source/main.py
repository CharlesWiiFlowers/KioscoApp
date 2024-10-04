from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(MDScreen):
    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")

class KioscoApp(MDApp):
    def build(self):
        return Builder.load_file('register_doctor.kv')

    def login(self, username, password):
        print(f"Usuario: {username}, Contraseña: {password}")
        self.nextSlide('register_doctor')

    def work(self):
        print("Yes, this work")

    def nextSlide(self, screen:str):
        """Change to your screen"""
        self.root.clear_widgets()
        otherScreen = Builder.load_file(f'{screen}.kv')
        self.root.add_widget(otherScreen)

if __name__ == '__main__':
    KioscoApp().run()
