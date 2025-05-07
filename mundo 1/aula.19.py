def obter_nome_pessoa(mensagem):
    """Solicita ao usuário um nome e valida a entrada."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        else:
            print("Entrada inválida. Por favor, digite um nome válido.")
            
def sortear_nomes(nomes):
    """sortear nomes aleatoriamente."""
    import random
    return random.choice(nomes)

def exibir_nome_sorteado(nome_sorteado):
    """Exibe o nome sorteado."""
    print(f"O nome sorteado foi: {nome_sorteado}")

def main():
    primeira_pessoa = obter_nome_pessoa("Digite o nome da primeira pessoa: ")
    segunda_pessoa = obter_nome_pessoa("Digite o nome da segunda pessoa: ")
    terceira_pessoa = obter_nome_pessoa("Digite o nome da terceira pessoa: ")
    quarta_pessoa = obter_nome_pessoa("Digite o nome da quarta pessoa: ")
    nomes = [primeira_pessoa, segunda_pessoa, terceira_pessoa, quarta_pessoa]
    nome_sorteado = sortear_nomes(nomes)
    exibir_nome_sorteado(nome_sorteado)
    
if __name__ == "__main__":
    main()