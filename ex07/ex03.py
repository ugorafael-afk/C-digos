# Aula 07 · Exercício 03 (casa, OBRIGATÓRIO): a classe Duracao com operadores
#
# Uma Duracao guarda um tempo em minutos: Duracao(90) é 1h 30min.
# minutos   @property e @minutos.setter. O setter RECUSA minutos negativos:
#               raise ValueError("minutos não podem ser negativos")
#           O __init__ recebe minutos e faz self.minutos = minutos: o setter
#           roda na criação.
# __add__   d1 + d2 RETORNA uma Duracao NOVA com a soma dos minutos.
#           Não mude o self. Se o outro não for Duracao, retorne NotImplemented.
# __eq__    d1 == d2 é True quando os minutos são iguais.
#           Se o outro não for Duracao, retorne NotImplemented.
# __lt__    d1 < d2 é True quando d1 tem MENOS minutos que d2.
#           Se o outro não for Duracao, retorne NotImplemented.
# __str__   retorna, por exemplo:  1h 30min   (horas com // 60, minutos com % 60)
# __repr__  retorna, por exemplo:  Duracao(90)
#
# SE TRAVAR, REVEJA:
#   __add__ ................ aula 07, slide 25   
#   não mudar o self ....... aula 07, slide 27  https://poo.leoad.com.br/aulas/aula-07/#s27
#   NotImplemented ......... aula 07, slide 30  https://poo.leoad.com.br/aulas/aula-07/#s30
#   __lt__ ................. aula 07, slide 36  https://poo.leoad.com.br/aulas/aula-07/#s36
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27


class Duracao:
    def __init__(self, minutos):
        self.minutos = minutos

    @property
    def minutos(self):
        return self._minutos

    @minutos.setter
    def minutos(self, valor):
        if valor < 0:
            raise ValueError("minutos não podem ser negativos")
        self._minutos = valor

    def __add__(self, outros):
       if isinstance(outros, Duracao):
           return Duracao(self.minutos + outros.minutos)
       return NotImplemented

    def __eq__(self, outros):
        if isinstance(outros, Duracao):
            return self.minutos == outros.minutos
        return NotImplemented

    def __lt__(self, outros):
       if isinstance(outros, Duracao):
           return self.minutos < outros.minutos
       return NotImplemented

    def __str__(self):
        return f"{self.minutos // 60}h {self.minutos % 60}min"

    def __repr__(self):
        return f"Duração({self.minutos})"

# ===== TESTE (não altere estas linhas) =====
class Qualquer:                     # pronta: diz que é igual a qualquer coisa
    def __eq__(self, outro):
        return True

d1 = Duracao(90)
d2 = Duracao(45)
d3 = d1 + d2

print(d3)                           # 2h 15min
print(d1, d2)                       # 1h 30min 0h 45min
print([d1, d2, d3])                 # [Duracao(90), Duracao(45), Duracao(135)]
print(d1.minutos, d2.minutos)       # 90 45
print(d1 + d2 == Duracao(135))      # True
print(d1 == d2)                     # False
print(d1 == 90)                     # False
print(d1 == Qualquer())             # True
print(d2 < d1, d1 < d2)             # True False
print(Duracao(60) < Duracao(60))    # False

erro_soma = "nenhum"
try:
    d1 + 5
except TypeError as erro:
    erro_soma = str(erro)
print("d1 + 5:", erro_soma)         # d1 + 5: unsupported operand type(s) for +: 'Duracao' and 'int'

erro_menor = "nenhum"
try:
    d1 < 5
except TypeError as erro:
    erro_menor = str(erro)
print("d1 < 5:", erro_menor)        # d1 < 5: '<' not supported between instances of 'Duracao' and 'int'

recusadas = 0
try:
    Duracao(-5)
except ValueError as erro:
    print("recusado:", erro)        # recusado: minutos não podem ser negativos
    recusadas = recusadas + 1
try:
    d2.minutos = -1
except ValueError:
    recusadas = recusadas + 1
print(recusadas, d2, Duracao(0))    # 2 0h 45min 0h 0min

print(f"chave: {(d3 + d1).minutos}-{len(str(d3 + d2))}-{len(repr(d2))}-{d1 + d2 == Duracao(135)}-{d1 == d2}-{d1 == 90}-{d1 == Qualquer()}-{Duracao(60) < Duracao(60)}-{d2 < d1}-{len(erro_soma)}-{len(erro_menor)}-{recusadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
# 2h 15min
# 1h 30min 0h 45min
# [Duração(90), Duração(45), Duração(135)]
# 90 45
# True
# False
# False
# True
# True False
# False
# d1 + 5: unsupported operand type(s) for +: 'Duracao' and 'int'
# d1 < 5: '<' not supported between instances of 'Duracao' and 'int'
# recusado: minutos não podem ser negativos
# 0h 45min 0h 0min
# chave: 225-7-11-True-False-False-True-False-True-54-58-2