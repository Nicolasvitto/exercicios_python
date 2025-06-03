"""
valor = float(input("digite o valor do produto R$"))
desconto = int(input("digite o valor do desconto: "))
valor1 = valor - (valor * desconto / 100)
print("=-"*28)
print("o prduto de valor R${} com desconto de {}%  vai  fica R${:.2f}".format(valor,desconto, valor1))
print("=-"*28)
"""

# ENTRADA DE INFORMÇÃO DO USUARIO
from util import receber_entrada


# CALCULA O DESCONTO DO PRODUTO
def produto_desconto(valor_pruduto,desconto_produto):
    return  valor_pruduto - (valor_pruduto * desconto_produto / 100)


# FUNÇÃO PRINCIPAL
def main():
    
    valor_produto = receber_entrada("Digite o valor do Produto R$: ")
    desconto_produto = receber_entrada("Digite quanto % , e o desconto do produto: ")
    
    print('=-'*28)
    print(f"O produto do valor R${valor_produto} com desconto de {desconto_produto}%  vai ficar {produto_desconto(valor_produto,desconto_produto):.2f}")
    print('=-'*28)
    
    
if __name__ == "__main__":
    main()