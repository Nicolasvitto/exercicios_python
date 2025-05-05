frase = str(input('digite uma frase: ')).upper().strip() #upper joga a string para maiculo
print('a letra A aparece {} vezes na frase.'.format(frase.count('A')))  #frase.count usado para contar a quantidade de letras na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))  # find da a posição na qual a letra aparece 
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # rfind ele procura a posição da letra pelo lado direito
# strip remove os espaços das letras 