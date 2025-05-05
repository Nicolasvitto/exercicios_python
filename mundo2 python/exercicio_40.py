def pegar_notas():
    """
    Função para pegar as notas do usuário.
    """
    while True:
        try:
            nota = float(input("Digite a nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def calcular_media(nota1, nota2):
    """
    Função para calcular a média entre duas notas.
    """
    return (nota1 + nota2) / 2
# Pegar as notas do usuário
nota1 = pegar_notas()
nota2 = pegar_notas()
# Calcular a média
media = calcular_media(nota1, nota2)
# Exibir a média

def verificar_aprovacao(media):
    """
    Função para verificar se o aluno foi aprovado, reprovado ou se está de recuperação.
    """
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media <= 6.9:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"
# Exibir o resultado    

def main():
    """
    Função principal que executa o programa.
    """
    print("\n--- Cálculo de Média ---")
    print(f"Nota 1: {nota1:.2f}")
    print(f"Nota 2: {nota2:.2f}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {verificar_aprovacao(media)}")
    print("\n--- Fim do programa ---")

if __name__ == "__main__":
    main()
# O código foi reestruturado para melhorar a legibilidade e a modularidade. As funções foram criadas para separar as responsabilidades, facilitando a manutenção e o entendimento do código. Além disso, foram adicionados comentários para explicar cada parte do código.