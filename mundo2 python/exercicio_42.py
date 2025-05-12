'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
def pegar_medida(mensagem):
     return float(input(mensagem))

def validar_mensagem_usuario(mensagem):
    while True:
        try:
            return pegar_medida(mensagem)
        except ValueError:
            print("por favor, entre com um valor válido.")


def pegar_tipo_triangulo(lado_direito, lado_esquerdo, lado_baixo):
    if lado_direito < lado_esquerdo + lado_baixo and lado_esquerdo < lado_direito + lado_baixo and lado_baixo < lado_direito + lado_esquerdo:
        print("os segmentos acima podem formar um triangulo", end='') 
        if lado_direito == lado_esquerdo and lado_esquerdo == lado_baixo:
            print("triangulo EQUILÁTERO")
        elif lado_direito == lado_esquerdo or lado_direito == lado_baixo or lado_esquerdo == lado_baixo:
            print("trinagulo ISÓSCELES")
        elif lado_direito != lado_esquerdo and lado_esquerdo != lado_baixo:
            print("trinagulo ESCALENO")
    else:
        print("os lados não podem formar um triangulo")
  

def main():
    lado_direito = validar_mensagem_usuario ('digite a primeira medida: ')
    lado_esquerdo = validar_mensagem_usuario ('digite o lado esquerdo do trinagulo: ')
    lado_baixo = validar_mensagem_usuario ('digite o lado de baixo do trinagulo: ')
    pegar_tipo_triangulo(lado_direito,lado_esquerdo,lado_baixo)

if __name__ == "__main__":
    main()



