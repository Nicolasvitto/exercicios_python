from Usuario import Usario_mensagem

class Tratamento_Erro_Usuario:
    @staticmethod
    def validar_mensagem(mensagem):
        while True:
            try:
                return Usario_mensagem.pegar_mensagem(mensagem)
            except ValueError:
                print("Por favor, entre com um valor válido.")
