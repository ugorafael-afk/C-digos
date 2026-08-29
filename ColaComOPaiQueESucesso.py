class Equipamento:
   
    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio
        self.disponil = True

    def exibir_dados(self):
        status = "Disponil" if self.disponil else "Emprestado"
        return f"{self.patrimonio} - {self.nome} - {status}"
        
notebook = Equipamento("notebook Dell", "PAT-001")
projetor = Equipamento("Projetor Epson", "PAT-002")

print(notebook.exibir_dados())
print(projetor.exibir_dados())