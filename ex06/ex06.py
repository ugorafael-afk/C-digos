# Aula 06 · Exercício 06 (casa, opcional): o zoológico e o isinstance
#
# Animal: o __init__ recebe nome e guarda.
# Mamifero é um Animal. Cachorro é um Mamifero. Peixe é um Animal.
#   (essas três só herdam: o corpo de cada uma é só pass)
#
# Zoologico NÃO herda de Animal: um zoológico não é um animal, ele TEM animais.
#   O __init__ recebe nome e cria self.animais = [].
#   adicionar(animal)   coloca o animal na lista.
#   contar_mamiferos()  RETORNA quantos animais da lista são Mamifero (for e isinstance).
#                       Atenção: um Cachorro também é um Mamifero.
#   nomes_dos_peixes()  RETORNA uma lista nova com os nomes dos Peixe.
#   __str__             retorna, por exemplo:  Zoo de Goiânia: 4 animais
#
# Exemplo: com Cachorro("Rex"), Mamifero("Baleia"), Peixe("Nemo") e Peixe("Dori")
# adicionados ao Zoologico("Zoo de Goiânia"):
#   contar_mamiferos  retorna 2
#   nomes_dos_peixes  retorna ['Nemo', 'Dori']
#
# Teste você mesmo: no fim do arquivo, monte o zoológico do exemplo e mostre
# os resultados com print.
#
# SE TRAVAR, REVEJA:
#   herança ................ aula 06, slide 5  https://poo.leoad.com.br/aulas/aula-06/#s5
#   isinstance ............. aula 06, slide 35  https://poo.leoad.com.br/aulas/aula-06/#s35
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Animal:
    def __init__(self, nome):
        self.nome = nome

class Mamifero(Animal):
    pass
class Cachorro(Mamifero):
    pass
class Peixe(Animal):
    pass

class Zoologico:
    def __init__(self, nome):
        self.nome = nome
        self.animal = []

    def adicionar(self, animal):
        self.animal.append(animal)

    def contar_mamiferos(self):
        contar = 0
        for animal in self.animal:
            if isinstance(animal, Mamifero):
                contar += 1
        return contar

    def nomes_dos_peixes(self):
        nomes = []
        for animal in self.animal:
            if isinstance(animal, Peixe):
                nomes.append(animal.nome)
        return nomes

    def __str__(self):
        return f"{self.nome}: {len(self.animal)} animais"

zoo = Zoologico("Zoo de Goiânia")
zoo.adicionar(Cachorro("Rex"))
zoo.adicionar(Mamifero("Baleia"))
zoo.adicionar(Peixe("Nemo"))
zoo.adicionar(Peixe("Dori"))
print(zoo.contar_mamiferos())
print(zoo.nomes_dos_peixes())
print(zoo)
        
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# 2
# ['Nemo', 'Dori']
# Zoo de Goiânia: 4 animais
