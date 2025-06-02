def receber_entrada(mensagem="Digite algo: "):
    entrada = input(mensagem).strip()
    
    # Tenta converter para int
    try:
        return int(entrada)
    except ValueError:
        pass

    # Tenta converter para float
    try:
        return float(entrada)
    except ValueError:
        pass

    # Se não for número, retorna como string
    return entrada
