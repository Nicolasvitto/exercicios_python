# biblioteca de chamar input 
from util import receber_entrada

# CALCULA O DOBRO DO VALOR
def dobro(numero):
   return numero * 2

# CALCULA O TRIPLO DO VALOR
def triplicação(numero):
    return numero * 3

# CALCULA A RAIZ DO VALOR
def raiz (numero):
    return numero ** (1/2)

def main():
    
    numero = receber_entrada("digite um numero: ")
    
    print(f"Dobro: {dobro(numero)}")
    print(f"Triplo: {triplicação(numero)}")
    print(f"Raiz: {raiz(numero)}")

if __name__=="__main__":
    main()