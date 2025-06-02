class sanduiche: 
    """
    Representa o produto final: um sanduiche com pão, recheio e molho.
    """
    def __init__(self, pao, recheio, molho):
        """
        Inicializa o sanduiche com pão, recheio e molho.
        """
        self.pao = pao
        self.recheio = recheio
        self.molho = molho

    def __str__(self):
        """
        retorna uma representação em string do sanduiche.
        """
        return f'Sanduiche com {self.pao}, {self.recheio} e {self.molho}.'
    
# Builder abstrato

class SanduicheBuilder:
    """
    Classe abstrata que define a interface para construir um sanduiche.
    """
    def __init__(self):
        """
        inicializa um novo objeto Sanduiche.
        """
        self.sanduiche = sanduiche(None, None, None)
        
    def preparar_pao(self):
        """
        Método abstrato para preparar o pão.
        """
        pass
    
    def preparar_recheio(self):
        """
        Método abstrato para preparar o recheio.
        """
        pass
    
    def preparar_molho(self):
        """
        Método abstrato para preparar o molho.
        """
        pass
    
    def get_sanduiche(self):
        """
        Retorna o sanduiche preparado.
        """
        return self.sanduiche
    
class SanduicheVegetarianoBuilder(SanduicheBuilder):
    """
    Construtor para sanduiches vegetarianos.
    """
    def preparar_pao(self):
        """
        Prepara o pão para o sanduiche vegetariano.
        """
        self.sanduiche.pao = 'Pão integral'
    
    def preparar_recheio(self):
        """
        Prepara o recheio para o sanduiche vegetariano.
        """
        self.sanduiche.recheio = 'Vegetais grelhados'
    
    def preparar_molho(self):
        """
        Prepara o molho para o sanduiche vegetariano.
        """
        self.sanduiche.molho = 'Molho de iogurte'

class SanduicheCarneBuilder(SanduicheBuilder):
    """
    Construtor para sanduiches de carne.
    """
    def preparar_pao(self):
        """
        Prepara o pão para o sanduiche de carne.
        """
        self.sanduiche.pao = 'Pão francês'
    
    def preparar_recheio(self):
        """
        Prepara o recheio para o sanduiche de carne.
        """
        self.sanduiche.recheio = 'Carne grelhada'
    
    def preparar_molho(self):
        """
        Prepara o molho para o sanduiche de carne.
        """
        self.sanduiche.molho = 'Molho barbecue'

#diretor
class SanduicheDirector:
    """
    Classe responsável por construir o sanduiche usando o builder.
    """
    def __init__(self, builder):
        """
        Inicializa o diretor com um builder.
        """
        self.builder = builder
    
    def construir_sanduiche(self):
        """
        Constrói o sanduiche usando o builder.
        """
        self.builder.preparar_pao()
        self.builder.preparar_recheio()
        self.builder.preparar_molho()
        return self.builder.get_sanduiche()
    
def get_sanduiche(mensagem):
    return input(mensagem).strip()

def validate_sanduiche(mensagem):
    while True:
        escolha = get_sanduiche(mensagem)
        if escolha in ['1', '2']:
            return escolha
        else:
            print("Opção inválida. Tente novamente.")
            
def main():

    print("Escolha o tipo de sanduíche:")
    print("1. Vegetariano")
    print("2. Carne")
    
    tipo = validate_sanduiche('Digite 1 ou 2: ')

    if tipo == '1':
        builder = SanduicheVegetarianoBuilder()
    else:
        builder = SanduicheCarneBuilder()

    diretor = SanduicheDirector(builder)
    sanduiche = diretor.construir_sanduiche()
    print(sanduiche)
     

if __name__ == "__main__":
    main()