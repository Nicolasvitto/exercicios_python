import random 
n1 = str(input("digite o primeiro nome: "))
n2 = str(input("digite o segundo nome: "))
n3 = str(input("digite o terceiro nome: "))
n4 = str(input("digite o quarto nome: "))
alunos = [n1, n2, n3, n4]
sorteio = random.choice(alunos)
print("o aluno sorteado foi: ", sorteio)