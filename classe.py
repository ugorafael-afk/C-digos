class Equipamentos:
    def exibir_dados(self):
        print("Nome: {self.nome}")
        print("Patrimonio: {self.patrimonio}")

notebook = Equipamentos()

notebook.nome = "notebook Dell"
notebook.patrimonio = "PAT_001"

notebook.exibir_dados()
