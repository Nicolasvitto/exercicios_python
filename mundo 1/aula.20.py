# pega nome dos alunos
def get_name(mensagem):
    return str(input(mensagem))


# função que trata o erro de mensagem
def error_handling(mensagem):
    while True:
        try:
            return get_name(mensagem)
        except ValueError:
            print("por favor coloque um nome valido")

def  main():
    from random import shuffle
    
    aluno1 = error_handling('digite o nome do promeiro aluno: ')
    aluno2 = error_handling('digite o nome do segundo aluno: ')
    aluno3 = error_handling('digite o nome do terceiro aluno: ')
    aluno4 = error_handling('digite o nome do quarto aluno: ')
    
    alunos = [aluno1, aluno2, aluno3, aluno4]
    
    # sorteia os alunos
    shuffle(alunos)
    
    # sapara por espaço e vigula
    joint = ', '.join(alunos)
    print(joint)
    
if __name__ == "__main__":
    main()