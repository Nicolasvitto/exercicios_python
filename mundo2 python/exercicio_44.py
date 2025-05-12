"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""

def get_message(message):
    return float(input(message))

def validate_message(message):
    while True:
        try:
            return get_message(message)
        except ValueError:
            print("Por favor, insira um valor válido.")

def PaymentMethod(purchase_price, payment_option):
    if payment_option == 1:
        return purchase_price - (purchase_price * 0.1)
    elif payment_option == 2:
        return purchase_price - (purchase_price * 0.05)
    elif payment_option == 3:
        return purchase_price
    elif payment_option == 4:
        return purchase_price + (purchase_price * 0.2)
    else:
        return "Opção de pagamento inválida."

def main():
    purchase_price = validate_message('Digite o preço da compra: ')
    print('''Escolha a forma de pagamento:
    [1] À vista dinheiro/cheque (10% de desconto)
    [2] À vista no cartão (5% de desconto)
    [3] Em até 2x no cartão (sem desconto)
    [4] 3x ou mais no cartão (20% de juros)''')
    payment_option = validate_message('Sua opção: ')
    final_price = PaymentMethod(purchase_price, payment_option)
    print(f'O preço final é: {final_price}')
    
    
if __name__ == "__main__":
    main()
