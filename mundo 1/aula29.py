velocidade = float(input('qual a velocidade do seu carro: '))

velocidade_acima = velocidade - 80

multa = 7 * velocidade_acima

if velocidade > 80:
    print('você execedeu o limite de velocidade de 80 KM, foi multado em R${}'.format(multa))
print('dirija com segurança')