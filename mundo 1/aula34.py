salario = float(input('digite seu salario R$ '))
if salario > 1250:
    print('houve um aumento de 10% no seu salario que agora sera R${:.2f}'.format((salario * 10) / 100 + salario))
else:
    print('houve um aumento de 15% no seu salario que agora sera R${:.2f}'.format((salario * 15) / 100 + salario))