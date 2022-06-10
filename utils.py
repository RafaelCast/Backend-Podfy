import os
from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'resizable', False) #Redimensionamento de janela
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (360, 800)

class WindowManager (ScreenManager):
    #Classe Root que vai lidar com transição de Screens
    pass

#ADICIONAR RECONHECIMENTO DE LOGIN VÁLIDO COMO FOI FEITO NA CLASSE "RegisterScreen(Screen)"
class LoginScreen(Screen):
    pass

class CustomizeScreen(Screen):
    pass