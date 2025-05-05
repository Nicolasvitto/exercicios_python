print('''1 para saber o rendimento
2 para ver quanto vai custar
3 para ver tudo ''')
escolha = int(input('Qual a sua escolha? '))
FLLvalor = float(input('digite o valor do fundo R$ '))
rendimentoFLL = float(input('digite o rendimento do fundo R$ '))
quantidedeFLL = int(input('quantidade que você vai comprar: '))

rendiemntof = rendimentoFLL * quantidedeFLL
valorf = FLLvalor * quantidedeFLL

if escolha == 1:
    print(f'O rendimento dos {quantidedeFLL} fundos é R${rendiemntof:.2f}')
elif escolha == 2:
    print(f'O valor do fundo é R${valorf:.2f}')
elif escolha == 3:
    print(f'O rendimento dos {quantidedeFLL} fundos é R${rendiemntof:.2f}')
    print(f'O valor do fundo que você devera investir é R${valorf:.2f}')
else:
    print('opção invalida')