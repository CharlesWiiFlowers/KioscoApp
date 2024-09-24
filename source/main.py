from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('login.kv')

# Simulamos una pantalla de inicio de sesión
class LoginScreen(Screen):
    def login(self, username, password):
        # Aquí podrías agregar la lógica de autenticación real
        if username == "doctor" and password == "12345":
            self.ids.login_status.text = "Inicio de sesión exitoso"
        else:
            self.ids.login_status.text = "Nombre de usuario o contraseña incorrectos"

class KioscoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        #Window.clearcolor = (1, 1, 1, 1)  # Color de fondo blanco
        return sm

if __name__ == '__main__':
    KioscoApp().run()