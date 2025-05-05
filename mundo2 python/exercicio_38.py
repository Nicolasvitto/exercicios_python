def obter_numero(mensagem):
    """Solicita ao usuário um número inteiro e valida a entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    primeiro_numero = obter_numero('Digite o primeiro número: ')
    segundo_numero = obter_numero('Digite o segundo número: ')

    if primeiro_numero > segundo_numero:
        print(f"O primeiro número ({primeiro_numero}) é maior que o segundo número ({segundo_numero}).")
    elif segundo_numero > primeiro_numero:
        print(f"O segundo número ({segundo_numero}) é maior que o primeiro número ({primeiro_numero}).")
    else:
        print(f"Os dois números são iguais: {primeiro_numero}.")

if __name__ == "__main__":
    main()