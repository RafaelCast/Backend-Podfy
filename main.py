from utils import * #importa todas as classes do arquivo classController.py

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


GUI = Builder.load_file("screen_manager.kv")
GUI = Builder.load_file("cadastro.kv")
GUI = Builder.load_file("customizacao.kv")

class Podfy(App):

    #Importação de recursos
    podfy_logo_white = os.path.join ('resources', 'podfy-logo-whitebg.jpg')
    inter_regular = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Regular.ttf')
    inter_medium = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Medium.ttf')
    inter_semibold = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-SemiBold.ttf')
    inter_bold = os.path.join('resources', 'fontes', 'Inter', 'static', 'Inter-Bold.ttf')

    user_icon = os.path.join('resources','img','profile_icon.png')
    user_icon_hover = os.path.join('resources','img','profile_icon_hover.png')

    def build(self):
        sm = WindowManager()
        # sm.current = 'login_screen'
        sm.current = 'login_screen' #Tela padrão que o WindowManager vai iniciar
        return sm


#Só vai rodar a aplicação se este arquivo (main.py) for executado individualmente (Ou seja, dando um "python main.py"). Se for importado e executado através de outro arquivo, não vai executar o conteúdo da função abaixo!
if __name__ == '__main__':
    Podfy().run()
