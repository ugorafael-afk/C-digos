class Equipamento:
    def __init__(self, custo, nome):
        self.custo = custo
        self.nome = nome

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):
        if novo_custo < 0:
            print("Erro: o custo não pode ser negativo")
            return

        self.__custo = novo_custo
        print("O custo não pode esta negativo")

    def exibir_informacao(self):
        print("\nDADOS DO EQUIPAMENTO")
        print(f"Nome: {self.nome}")
        print(f"Custo: R$ {self.custo}")


equipamento = Equipamento(3500, "Computador")

print("\nAlterando o custo do equipamento para 4000")
equipamento.custo = 4000
equipamento.exibir_informacao()

print("\nAlterando o custo do equipamento para -5000")
equipamento.nome = ""
equipamento.custo = -5000
equipamento.exibir_informacao()