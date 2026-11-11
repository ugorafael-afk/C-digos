from abc import ABC, abstractmethod

class ImovelNaoEncontradoError(Exception):
    pass

class Imovel(ABC):
    def __init__(self, codigo, endereco, area):
        self.codigo = codigo
        self.endereco = endereco
        self.area = area

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor <= 0:
            raise ValueError("O código do imóvel deve ser maior que zero")
        self._codigo = valor

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
        return f"('{self.codigo}'), ('{self.endereco}'), ('{self.aluguel()}'), ('{self.area}')"

class Casa(Imovel):
    def __init__(self, codigo, endereco, area, quintal):
        super().__init__(codigo, endereco, area)
        self.quintal = quintal

    def aluguel(self):
        return 30 * self.area + (250 if self.quintal else 0)


class Apartamento(Imovel):
    def __init__(self, codigo, endereco, area, condominio):
        super().__init__(codigo, endereco, area)
        self.condominio = condominio

    def aluguel(self):
        return 20 * self.area + self.condominio

class Kitnet(Imovel):
    def __init__(self, codigo, endereco, area):
        super().__init__(codigo, endereco, area)

    def aluguel(self):
        return 15 * self.area


class Imobiliaria:
    def __init__(self):
        self.imoveis = []

    def adicionar(self, imovel):
        self.imoveis.append(imovel)

    def buscar(self, codigo):
        for imovel in self.imoveis:
            if imovel.codigo == codigo:
                return imovel
        raise ImovelNaoEncontradoError(f"Imóvel com código {codigo} não foi encontrado")

    def total_alugueis(self):
        total = 0
        for imovel in self.imoveis:
            total += imovel.aluguel()
        return total


imobiliaria = Imobiliaria()

casa1 = Casa(1, "Rua das Flores, 123", 100, True)
apt1 = Apartamento(2, "Av. Paulista, 500", 50, 270)
kit1 = Kitnet(3, "Rua Central, 45", 20)

imobiliaria.adicionar(casa1)
imobiliaria.adicionar(apt1)
imobiliaria.adicionar(kit1)

print(casa1) # SAÍDA: O endereço Rua das Flores, 123, com o custo de aluguel 3250 R$. Está a venda, com uma area de 100 m²
print(apt1) # SAÍDA: O endereço Av. Paulista, 500, com o custo de aluguel 1270 R$. Está a venda, com uma area de 50 m²
print(kit1) # SAÍDA: O endereço Rua Central, 45, com o custo de aluguel 300 R$. Está a venda, com uma area de 20 m²

print(imobiliaria.buscar(2)) # SAÍDA: O endereço Av. Paulista, 500, com o custo de aluguel 1270 R$. Está a venda, com uma area de 50 m²
print(imobiliaria.total_alugueis()) # SAÍDA: 4820

try:
    imobiliaria.buscar(99)
except ImovelNaoEncontradoError as e:
    print(e) # SAÍDA: Imóvel com código 99 não foi encontrado

try:
    kit_invalida = Kitnet(4, "Rua X", 5)
except ValueError as e:
    print(e) # SAÍDA: O valor da area está incorreto. Deve ser maior que 10 se não já não é nem Kitnet, já é barraco e ninguem quer morar em um barraco eu acho