'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

def pegar_medida(mensagem):
     while True:
        try:
            return float(input(mensagem))
        except ValueError: 
            print("entre com um valor valido")


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
    lado_direito = pegar_medida('digite a primeira medida: ')
    lado_esquerdo = pegar_medida('digite o lado esquerdo do trinagulo: ')
    lado_baixo = pegar_medida('digite o lado de baixo do trinagulo: ')
    pegar_tipo_triangulo(lado_direito,lado_esquerdo,lado_baixo)

if __name__ == "__main__":
    main()



