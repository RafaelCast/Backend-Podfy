
import os
import re
from datetime import date
from xmlrpc.client import Boolean

#Importações Kivy
from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'resizable', False) #Redimensionamento de janela
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList

#importações KivyMD
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import HoverBehavior
from kivymd.theming import ThemableBehavior
from kivymd.theming import ThemeManager





# importações BD
from flask import Flask, request as flask_request
import sqlite3 as sql

# importações crypt
import Back.Crypt

# importações Cadastro
from Back.Cadastro import *





#SOBREPOSIÇÃO DE CORES-PADRÃO DO KIVYMD
colors = {
    "Yellow": {
        "50": "FEC200", ##Amarelo padrão podfy
        "100": "252525", #lighter black padrão podfy
        "200": "121212", #Dark Black padrão podfy
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}