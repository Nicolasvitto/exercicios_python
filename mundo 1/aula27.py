frase = input(str('digite seu nome: ')).strip
palavra = frase.split() # split divide a frase em partes
print('seu primeiro nome e {}'.format(palavra[0])) # a variavel palavra e numerada com o primeiro e ultima frase da lista
print('seu ultimo nome e {}'.format(palavra[-1]))

