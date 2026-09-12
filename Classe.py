class Equipamentos:
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Patrimonio: {self.patrimonio}")

notebook = Equipamentos()

notebook.nome = "notebook Dell"
notebook.patrimonio = "PAT_001"

if not notebook.nome.strip():
    raise ValueError("O nome do equipamento não pode ser vazio")

if not notebook.patrimonio.startswith("PAT_001"):
    raise ValueError("O patrimônio do equipamento não pode ser vazio")

notebook.exibir_dados()