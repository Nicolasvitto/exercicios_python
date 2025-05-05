km = float(input('digite a distancia da sua viagem: '))

if km <= 200:
    print(f'preço da passagem é R${km * 0.5:.2f}')
else:
    print(f'preço da passagem é R${km * 0.45:.2f}')
