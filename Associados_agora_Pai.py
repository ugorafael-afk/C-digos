class Tecnico:
    def __init__(self, nome, especializacao):
        self.nome = nome
        self.especializacao = especializacao

    def exibir_manutencao(self, equipamento):
        print(f"O Tecnico {self.nome}, especializado em {self.especializacao}," 
               f" levou a {equipamento.nome} para a manutenção ")

class Equipamento:
    def __init__(self, nome):
        self.nome = nome

    def exibir_tecnico(self, tecnico):
        print(f"O equipamento da {self.nome}, foi levado para a manutenção pelo " 
               f"{tecnico.nome}, especializado em {tecnico.especializacao}")


tecnico1 = Tecnico("Ugo", "ADS")
tecnico2 = Tecnico("Edelso", "Cozinhar")

equipamento1 = Equipamento("ASUS")
equipamento2 = Equipamento("Panela")

tecnico1.exibir_manutencao(equipamento1)
tecnico2.exibir_manutencao(equipamento2)
print(" ")
equipamento1.exibir_tecnico(tecnico1)
equipamento2.exibir_tecnico(tecnico2)
print(" ")
print(tecnico1.nome)
print(tecnico2.nome)
print(equipamento1.nome)
print(equipamento2.nome)