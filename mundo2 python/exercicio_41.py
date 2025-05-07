def pegar_data_nascimento():
    """
    Função para pegar a data de nascimento do usuário.
    """
    while True:
        try:
            dia = int(input("Digite o dia de nascimento: "))
            mes = int(input("Digite o mês de nascimento: "))
            ano = int(input("Digite o ano de nascimento: "))
            return dia, mes, ano
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            
def calcular_idade(dia, mes, ano):
    """
    Função para calcular a idade com base na data de nascimento.
    """
    from datetime import date
    hoje = date.today()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
    return idade
# Pegar a data de nascimento do usuário

def verificar_categoria(idade):
    """
    Função para verificar a categoria do atleta com base na idade.
    """
    if idade <= 9:
        return "MIRIM"
    elif idade <= 14:
        return "INFANTIL"
    elif idade <= 19:
        return "JÚNIOR"
    elif idade <= 25:
        return "SÊNIOR"
    else:
        return "MASTER"
# Exibir a categoria do atleta
def main():
    """
    Função principal que executa o programa.
    """
    print("\n--- Cálculo de Idade ---")
    dia, mes, ano = pegar_data_nascimento()
    idade = calcular_idade(dia, mes, ano)
    print(f"Idade: {idade} anos")
    print(f"Categoria: {verificar_categoria(idade)}")
    print("\n--- Fim do programa ---")
    
if __name__ == "__main__":
    main()

    