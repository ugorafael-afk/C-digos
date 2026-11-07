# Aula 08 · Exercício 07 (casa, opcional): produtos com imposto
#
# Crie a classe abstrata Produto (herda de ABC):
#   __init__(nome, preco)   guarda o nome e faz self.preco = preco
#                           (assim o setter já confere o preço).
#   preco         property concreta com setter: se o valor for negativo,
#                 raise ValueError("o preço não pode ser negativo").
#                 Guarde o valor em self._preco.
#   imposto       property ABSTRATA: o imposto em porcentagem (5 quer dizer 5%).
#   preco_final   property concreta: RETORNA preco + preco * imposto / 100.
#   __str__       retorna, por exemplo:  Fone: R$ 115.00 (imposto de 15%)
#                 (o preco_final com :.2f)
#   de_texto      @classmethod: recebe "Arroz;20" e RETORNA o produto, com o
#                 preço como float. Use cls(...): chamado pela filha, o cls
#                 é a filha. Alimento.de_texto("Arroz;20") cria um Alimento.
#
# E as duas filhas, com imposto como property:
# Alimento     imposto 5
# Eletronico   imposto 15
#
# Exemplos:
#   Alimento("Arroz", 20).preco_final     21.0
#   Eletronico("Fone", 100).preco_final   115.0
#   print(Eletronico("Fone", 100))        Fone: R$ 115.00 (imposto de 15%)
#   Eletronico("Cabo", -5)   ValueError: o preço não pode ser negativo
#   print(Alimento.de_texto("Arroz;20"))   Arroz: R$ 21.00 (imposto de 5%)
#
# No teste, tente criar Eletronico("Cabo", -5) dentro de um
# try/except ValueError e, no except, imprima Preço recusado.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   property abstrata ...... aula 08, slide 21  https://poo.leoad.com.br/aulas/aula-08/#s21
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("o preço não pode ser negativo")
        self._preco = valor

    @property
    @abstractmethod
    def imposto(self):
        pass

    def preco_final(self):
        return self.preco + self.preco * self.imposto / 100

    def __str__(self):
        return f"{self.nome}: R$ {self.preco_final():.2f} (Imposto de {self.imposto}%)"

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))

class Alimento(Produto):
    @property
    def imposto(self):
        return 5

class Eletronico(Produto):
    @property
    def imposto(self):
        return 15

a1 = Alimento("Arroz", 20)
e1 = Eletronico("Fone", 100)

print(a1.preco_final())
print(e1.preco_final())
print(e1)
print(Alimento.de_texto("Arroz;20"))

try:
    e2 = Eletronico("Cabo", -5)
except ValueError:
    print("Preço recusado.")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# 21.0
# 115.0
# Fone: R$ 115.00 (Imposto de 15%)
# Arroz: R$ 21.00 (Imposto de 5%)
# Preço recusado.