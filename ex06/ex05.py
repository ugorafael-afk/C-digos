# Aula 06 · Exercício 05 (casa, OBRIGATÓRIO): o cardápio de pizzas
#
# Pizza: o __init__ recebe sabor e preco.
#   preco          @property e @preco.setter. O setter RECUSA preço negativo:
#                      raise ValueError("preço não pode ser negativo")
#                  O __init__ faz self.preco = preco: o setter roda na criação.
#   preco_final()  RETORNA o preco.
#   __str__        retorna, por exemplo:  Calabresa: R$ 40.00
#                  (use self.preco_final() no texto, não self.preco)
#
# PizzaGrande é uma Pizza:
#   preco_final()  ESTENDE o do pai: o preço do pai (super()) mais 50%.
#   __str__        ESTENDE o do pai:  Calabresa: R$ 60.00 (grande)
#
# PizzaDoDia é uma Pizza:
#   preco_final()  SUBSTITUI o do pai: sempre 29.9, seja qual for o preco.
#   Exemplo: PizzaDoDia("Frango", 45) aparece como  Frango: R$ 29.90
#
# Teste você mesmo: no fim do arquivo, crie uma pizza de cada tipo e mostre
# as três com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que PizzaGrande("Atum", -10) é recusada: a filha herda o setter.
#
# SE TRAVAR, REVEJA:
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Pizza:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preço não pode ser negativo")
        self._preco = valor

    def preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.sabor}: R$ {self.preco_final()}"

class PizzaGrande(Pizza):

    def preco_final(self):
        return super().preco_final() / 0.5

    def __str__(self):
        return f"{self.sabor}: R$ {self.preco_final()}"

class PizzaDoDia(Pizza):
    def preco_final(self):
        return 29.9

    def __str__(self):
        return f"{self.sabor}: R$ {self.preco_final()}"

p1 = Pizza("Quatro Queijo", 45)
p2 = PizzaGrande("Calabresa", 40)
p3 = PizzaDoDia("Portuguesa", 45)
print("========================")
print(p1)
print(p2)
print(p3)
try:
    PizzaGrande("atum", -10)
except ValueError:
    print("Estais erradeixão")
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# ========================
# Quatro Queijo: R$ 45
# Calabresa: R$ 80.0
# Portuguesa: R$ 29.9
# Estais erradeixão