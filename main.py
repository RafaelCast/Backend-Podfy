import os
from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'resizable', False) #Redimensionamento de janela
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior

Window.size = (360, 800)

class WindowManager (ScreenManager):
    #Classe Root que vai lidar com transição de Screens
    pass

class User:
    def __init__(self, email, cpf, senha):
        self.email = email
        self.cpf = cpf
        self.senha = senha


class RegisterScreen(Screen):
    email = ObjectProperty(None)
    confirm = ObjectProperty(None)
    cpf = ObjectProperty(None)
    senha = ObjectProperty(None)

    def btn(self):
        user = None

        if self.email.text == self.confirm.text and len(self.cpf.text) == 11:
            user = User(self.email.text, self.cpf.text, self.senha.text)
            App.get_running_app().stop()
            return user

        elif self.email.text != self.confirm.text or len(self.email.text) == 0:
            print("Email incorreto!")

        elif len(self.cpf.text) != 11:
            print("CPF inválido")



    def val(self):
            if self.email.text == self.confirm.text and len(self.cpf.text) == 11:
                user = User(self.email.text, self.cpf.text, self.senha.text)
                return user

            elif self.email.text != self.confirm.text or len(self.email.text) == 0:
                print("Email incorreto!")

            elif len(self.cpf.text) != 11:
                print("CPF inválido")


class LoginScreen(Screen):
    pass

GUI = Builder.load_file("cadastro.kv")
class Podfy(App):

    # podfy_logo_white = os.path.join ('resources', 'podfy-logo-whitebg.png') #Associa a logo com fundo branco com a variável podfy_logo_white
    podfy_logo_white = os.path.join ('resources', 'podfy-logo-whitebg.jpg') #Associa a logo com fundo branco com a variável podfy_logo_white

    #Associa as fontes com variáveis, para facilitar o uso posterior:
    inter_regular = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Regular.ttf')
    inter_medium = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Medium.ttf')
    inter_semibold = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-SemiBold.ttf')
    inter_bold = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Bold.ttf')
    
    def build(self):
        return WindowManager()


#Só vai rodar a aplicação se este arquivo (main.py) for executado individualmente (Ou seja, dando um "python main.py"). Se for importado e executado através de outro arquivo, não vai executar o conteúdo da função abaixo!
if __name__ == '__main__':
    Podfy().run()
