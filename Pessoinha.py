class Pessoa:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def exibir_dados(self):
        print(f"O/A Cidadão {self.nome}, possuindo a idade {self.idade}, especializado em {self.curso}")

    def fala(self):
        print(f"O/A {self.nome} disse que você fedi a titica de galinha, vai deixar? ")

pessoa1 = Pessoa("Ugo", 18, "ADS")
pessoa2 = Pessoa("Manu", 15, "Nada da vida")
pessoa3 = Pessoa("Wilton", 51, "ADS")

pessoa1.fala()
pessoa2.fala()
pessoa3.fala()
print(" ")
pessoa1.exibir_dados()
pessoa2.exibir_dados()
pessoa3.exibir_dados()