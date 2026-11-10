from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, endereco, area):
        self.endereco = endereco
        self.area = area

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        if valor == "":
            raise ValueError("O nome de endereço não pode estár vazio")
        self._endereco = valor

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, valor):
        if valor < 10:
            raise ValueError("O valor da area está incorreto. Deve ser maior que 10 se não já não é nem Kitnet, já é barraco e ninguem quer morar em um barraco eu acho")
        self._area = valor

    @abstractmethod
    def aluguel(self):
        pass

    def __str__(self):
        return f"O endereço {self.endereco}, com o custo de aluguel {self.aluguel()} R$. Está a venda, com uma area de {self.area} m²"

    def __repr__(self):
        return f"('{self.endereco}'), ('{self.aluguel()}'), ('{self.area}')"

class Casa(Imovel):
    def __init__(self, endereco, area, quintal):
        super().__init__(endereco, area)
        self.quintal = quintal

    def aluguel(self):
        return 30 * self.area + (250 if self.quintal else 0)


class Apartamento(Imovel):
    def __init__(self, endereco, area, condominio):
        super().__init__(endereco, area)
        self.condominio = condominio

    def aluguel(self):
        return 20 * self.area + 270 # Esse duzentos e setenta e do condominio

class Kitnet(Imovel):
    def __init__(self, endereco, area):
        super().__init__(endereco, area)

    def aluguel(self):
        return 15 * self.area  