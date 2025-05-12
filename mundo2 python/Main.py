from Tratamento_erro_usuario import Tratamento_Erro_Usuario
from triangulo import Triangulo
def Main():
    l1 = Tratamento_Erro_Usuario.validar_mensagem("Digite o primeiro lado: ")
    l2 = Tratamento_Erro_Usuario.validar_mensagem("Digite o segundo lado: ")
    l3 = Tratamento_Erro_Usuario.validar_mensagem("Digite o terceiro lado: ")

    t = Triangulo(l1, l2, l3)  
    print(t.tipo())  

if __name__ == "__main__":
    Main()
