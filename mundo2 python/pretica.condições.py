nome = str (input('Qual é seu nome? '))
if nome == 'nicolas':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no brasil')
else:
    print('seu nome e normal ')
print('tenha um bom dia, {}'.format(nome))
