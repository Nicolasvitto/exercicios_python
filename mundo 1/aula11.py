"""
largura = float(input("coloque a largura da parede: "))
altura = float(input("coloque a altura da parede: "))
area = largura * altura
tinta = area / 2
print("sua parede tem a dimensão de {} x {} e sua área é de {:.2f}".".format(largura, altura, area))
print("Para pintar a parede, você precisará de {:.2f}L de tinta.".format(tinta))
"""
from util import receber_entrada


def area (largura, altura):
   return largura * altura

def tinta(largura,altura):
    return area(largura, altura) / 2

def main():
    
    largura = receber_entrada("qual a largura da parade: ")
    altura = receber_entrada("qual a altura da parede: ")
    
    print(f"sua parede tem a dimensão de {largura} X {altura} e sua área é de {area(largura,altura):.2f}M²")
    print(f"para pintar a parade você precisa de {tinta(largura,altura):.2f}L de tinta ")
    
if __name__== "__main__":
    main()    