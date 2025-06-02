"""R = float(input("digite quanto você tem na carteira? R$:"))

C = R / 5.54

print("com {:.2f}R$ você podera comprar {:.2f} USD ".format(R, C))"""

from util import receber_entrada


# converte real para dolar
def converter_para_dolar(Real):
    return Real / 5.54

def main():
    
    Real = receber_entrada("Quantos Reais você tem R$: ")
    
    print(f"com R${Real} você podera comprar {converter_para_dolar(Real):.2f} USD")
    
if __name__ == "__main__":
    main()