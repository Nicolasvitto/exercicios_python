from util import receber_entrada

def numeros_pares(numero_usuario):
    contador = 0 
    while contador <= numero_usuario:
        print(contador)
        contador += 2
        
        
def main():
    
    print("numeros pares")
    
    numero_usuario = receber_entrada("digite um numero: ")
    
    numeros_pares(numero_usuario)

if __name__ == "__main__":
    main()