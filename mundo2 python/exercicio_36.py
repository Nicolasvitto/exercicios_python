salario = float(input('diigite seu salario: R$ '))
casa_valor = float(input('qual o valor da casa? R$ '))
anos = int(input('quantos anos de financiamento? '))
salario_porcentagem = salario * 30 / 100
prestacao = casa_valor / (anos * 12)
if prestacao <= salario_porcentagem:
    print('empréstimo pode ser concedido')
else:
    print('empréstimo negado')
# o valor da prestação não pode ser maior que 30% do salário ou então o empréstimo será negado.