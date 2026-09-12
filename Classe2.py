class Equipamento:

    def __init__(self, nome, patrimonio, disponivel = True, setor = "Não definido"):
        if not patrimonio.startswith("PAT-"):
            raise ValueError("O patrimônio é invalido")
        if not nome.strip():
            raise ValueError("O nome do equipamento é obrigatório")
        
        self.nome = nome
        self.patrimonio = patrimonio
        self.setor = setor
        self.disponivel = disponivel

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Patrimonio: {self.patrimonio}")
        print(f"Setor: {self.setor}")
        print(f"Disponível: {self.disponivel}")

try:
    notebook = Equipamento("notebook Dell", "PAT-001", True, "TI")
    notebook2 = Equipamento("notebook HP", "PAT-002", False, "financeiro")
    notebook.exibir_dados()
    notebook2.exibir_dados()
except ValueError as erro:
    print(f"Erro: {erro}")  