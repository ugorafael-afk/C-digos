class Equipamento:

    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Patrimonio: {self.patrimonio}")

notebook = Equipamento("notebook Dell", "PAT_001")
notebook.exibir_dados()