"""
salario = float(input("digite seu salario R$"))
salario_total  =  salario + (salario * 15) / 100
print(f"o seu salario total é R${salario_total:.2f}")
"""
# BIBLIOTECA DE ENTRADA DO USUARIO
from util import receber_entrada

# FUNÇÃO DE CALCULO DE SALARIO
def bonificação(salario):
    return salario + (salario * 15) / 100

#  FUNÇÃO PRINCIPAL
def main():
    
    print("CALCULO DE BONIFICAÇÃO DE SALARIO")
    
    salario = receber_entrada("digite quanto você ganha R$: ")
    
    print(f"o seu salario total é R${bonificação(salario):.2f}")
    
if __name__=="__main__":
    main()