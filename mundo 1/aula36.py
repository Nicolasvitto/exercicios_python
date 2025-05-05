casa = float(input('qual o valor do imovel R$ '))
salario = float(input('quanto você ganha R$ '))
anos = int(input('quantos anos de financiamento: '))

meses = anos * 12
prestacao = casa / meses
minimo = salario * 30 / 100
print('para pagar a casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
   print('Empréstimo pode ser concedido')
else:
    print('infelizmente o empréstimo não pode ser concedido')
