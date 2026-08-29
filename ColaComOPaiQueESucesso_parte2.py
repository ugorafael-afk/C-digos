class Equipamento:
   
    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio
        self.disponivel = True

    def exibir_dados(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f"{self.patrimonio} - {self.nome} - {status}"
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"{self.nome} Emprestado com Sucesso!"
        else:
            return f"Não foi possível Emprestar."

notebook = Equipamento("notebook Dell", "PAT-001")


print(notebook.exibir_dados())
print(notebook.emprestar())
print(notebook.exibir_dados())
print(notebook.emprestar())