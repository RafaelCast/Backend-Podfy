import os
import re
from tkinter import Tk

from tkinter.filedialog import askopenfilename
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
import pyrebase
from Back.Utils import *

api = Flask(__name__)

config = {
    "apiKey": "AIzaSyDAQg2_lUP349sJk9LwAo0AvrKXe9ybF-c",
    "authDomain": "podfy-354600.firebaseapp.com",
    "databaseURL": "https://podfy-354600-default-rtdb.firebaseio.com",
    "projectId": "podfy-354600",
    "storageBucket": "podfy-354600.appspot.com",
    "serviceAccount": "serviceAccountKey.json"
}


class UploadScreen(Screen):
    EnvEp = ObjectProperty(None)

    def selecionar_arquivo():
        janela_padrao = Tk().withdraw()
        caminho_do_arquivo = askopenfilename(filetypes=(("Arquivos de audio", "*.mp3"), ('Todos os arquivos', '*.*')))
        caminho_do_arquivo = Path(caminho_do_arquivo)
        if caminho_do_arquivo:
            print(caminho_do_arquivo)
            return caminho_do_arquivo

        else:
            print("Nenhum arquivo selecionado")

    def get_arquivo(dir):
        with os.scandir(dir) as entrie:
            yield entry
        pass

    def post_arquivo(self):
        #dirpath = UploadScreen.selecionar_arquivo()
        firebase_storage = pyrebase.initialize_app(config)
        storage = firebase_storage.storage()
        storage.child("Lista5.PDF").put('Lista5.pdf')
