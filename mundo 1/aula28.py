from random import randint # importa somente o randit da biblioteca random 
from time import sleep



numero = randint(0, 5)  # faz o computador escolher um numero de 0 a 5
print('-=-' * 20)
print('tente adivinhar o numero que eu pensei: ')
print('-=-' * 20)
numero_usuario = int(input('qual é o seu palpite? '))
print("PRECESSANDO....")
sleep(3) # faz o programa pausar por 3 segundos
# interação do usuario para adivinhar o numero

if numero_usuario == numero: 
    print('parabéns você acertou')
else:
    
    print('infelizmente você errou, o número que eu pensei era {}'.format(numero))
    
# exibe se o numero esta correto ou não.

