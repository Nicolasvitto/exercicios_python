def obter_idade(mensagem):
    """Solicita ao usuário um número inteiro e valida a entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            
def verificação_alistamento(alistou, idade):
    """Verifica o status de alistamento com base na resposta do usuário."""
    if alistou == 'sim':
        print("Você está alistado.")
    elif alistou == 'não':
        caso_não_alistamento(idade)
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

def caso_não_alistamento(idade):
    """Exibe mensagens com base na idade do usuário e no status de alistamento."""
    if idade < 18:
        print("Você ainda não pode se alistar.")
        print(f"Faltam {18 - idade} anos para você se alistar.")
    elif idade == 18:
        print("Você deve se alistar agora.")
    else:
        print("Você já passou do prazo para se alistar.")
        print(f"Você deveria ter se alistado há {idade - 18} anos.")

def main():
    """Função principal que executa o programa."""
    nome = input("Digite seu nome: ")
    idade = obter_idade("Digite sua idade: ")
    alistou = input("Você se alistou? (sim/não): ").strip().lower()
    verificação_alistamento(alistou, idade)

if __name__ == "__main__":
    main()