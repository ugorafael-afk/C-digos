class Animal:
    def __init__(self, raca, genero, idade):
        self.raca = raca
        self.genero = genero
        self.idade = idade

    def exibir_informacao(self):
        print(f"O/A {self.raca}, foi enviado para o Veterinario quando tinha "
              f"{self.idade}. Lá eles descobriram que o animal era {self.genero}")

    def andar(self):
        print(f"O/A {self.raca} estava correndo a mais de 70km por h")

animal1 = Animal("Iguana", "Macho", 11)
animal2 = Animal("Cavalo", "Macho", 6)
animal3 = Animal("Chita", "Femia", 2)

animal1.exibir_informacao()
animal2.exibir_informacao()
animal3.exibir_informacao()
print(" ")
animal1.andar()
animal2.andar()
animal3.andar()