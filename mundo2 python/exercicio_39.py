from datetime import date


def obter_ano_nascimento(mensagem):
    """Solicita ao usuário um número inteiro e valida a entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            
def verificação_alistamento(alistou, idade, ano_nascimento, ano_atual):
    """Verifica o status de alistamento com base na resposta do usuário."""
    if alistou == 'sim':
        print("Você está alistado.")
    elif alistou == 'não':
        caso_não_alistamento(ano_nascimento, idade, ano_atual)
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

def caso_não_alistamento(ano_nascimento,idade,ano_atual):
    """Exibe mensagens com base na idade do usuário e no status de alistamento."""
    if idade < 18:
        print("Você ainda não pode se alistar.")
        print(f"Faltam {18 - idade} anos para você se alistar.")
        print(f"Você deve se alistar em {ano_nascimento + 18}.")    
    elif idade == 18:
        print("Você deve se alistar agora.")
    else:
        print("Você já passou do prazo para se alistar.")
        print(f"Você deveria ter se alistado há {idade - 18} anos.")
        print(f"Você deveria ter se alistado em {ano_nascimento + 18}.")

def main():
    """Função principal que executa o programa."""
    nome = input("Digite seu nome: ")
    ano_nascimento = obter_ano_nascimento("Digite o Ano que nasceu: ")
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    alistou = input("Você se alistou? (sim/não): ").strip().lower()
    print(f"\n--- Dados do Alistamento ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Ano de nascimento: {ano_nascimento}")
    print(f"Ano atual: {ano_atual}")
    print(f"Status de alistamento: {alistou}")
    verificação_alistamento(alistou, idade, ano_nascimento, ano_atual)
    print("\n--- Fim do programa ---")
    
    
if __name__ == "__main__":
    main()