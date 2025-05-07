nome = str (input('Qual é seu nome? '))
if nome == 'nicolas':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no brasil')
else:
    print('seu nome e normal ')
print('tenha um bom dia, {}'.format(nome))

a = float(input("nota1: "))
b = float(input("nota2: "))
c = (a + b) / 2
if c >= 7:
    print("passou")
elif c >= 5:
    print("recuperacao")
else:
    print("reprovou")