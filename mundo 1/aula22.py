nome = str(input("digite um nome: "))
maisculo = nome.upper()
minusculo = nome.lower()
palavra = nome.split()
palavra2 = nome.replace(" ", "")
palavra1 = palavra[0]
todo1 = len(palavra2)
todo2  =  len(palavra1)
print("seu nome maisculo é {}".format(maisculo))
print("seu nome minusculo é {}".format(minusculo))
print("seu nome tem ao todo {} letras".format(todo1))
print("seu primeiro nome tem {} letras".format(todo2))