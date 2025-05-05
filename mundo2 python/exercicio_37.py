numero = int(input('digite um numero inteiro: '))
print('''escolha um dos sistemas para conversão:
      [1] binario
      [2] octal
      [3] hexadecimal
      ''')
opcao = int(input('sua opção: '))
if opcao == 1:
    print('{}convertido para binario é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('opção inválida. tente novamente')
# o programa converte um número inteiro para binário, octal ou hexadecimal, dependendo da escolha do usuário.