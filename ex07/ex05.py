# Aula 07 · Exercício 05 (casa, OBRIGATÓRIO): o Vetor completo
#
# O __init__ recebe x e y e guarda os dois.
# __add__   v1 + v2 RETORNA um Vetor NOVO: Vetor(1, 2) + Vetor(3, 4) dá Vetor(4, 6)
# __sub__   v1 - v2 RETORNA um Vetor NOVO: Vetor(5, 5) - Vetor(1, 2) dá Vetor(4, 3)
# __eq__    Vetor(1, 2) == Vetor(1, 2) dá True, e Vetor(1, 2) == 5 dá False
# __str__   retorna, por exemplo:  (4, 6)         print(v) usa este
# __repr__  retorna, por exemplo:  Vetor(4, 6)    print([v1, v2]) usa este
# Nos três operadores, se o outro não for Vetor, retorne NotImplemented.
# Nenhum operador muda o self: depois de v3 = v1 + v2, o v1 continua igual.
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois vetores e mostre
# os resultados com print. Use os exemplos acima para conferir.
# A ÚLTIMA linha do seu teste deve ser:  print(Vetor(1, 2) + 5)
# Ela tem que terminar em TypeError: unsupported operand type(s) for +: 'Vetor' and 'int'
# (é a última porque o programa para ali). Cole esse erro também na SAÍDA.
#
# SE TRAVAR, REVEJA:
#   __add__ ................ aula 07, slide 25  https://poo.leoad.com.br/aulas/aula-07/#s25
#   não mudar o self ....... aula 07, slide 27  https://poo.leoad.com.br/aulas/aula-07/#s27
#   NotImplemented ......... aula 07, slide 30  https://poo.leoad.com.br/aulas/aula-07/#s30
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        if isinstance(outro, Vetor):
            return Vetor(self.x + outro.x, self.y + outro.y)
        return NotImplemented

    def __sub__(self, outro):
        if isinstance(outro, Vetor):
            return Vetor(self.x - outro.x, self.y - outro.y)
        return NotImplemented

    def __eq__(self, outro):
        if isinstance(outro, Vetor):
            return self.x == outro.x and self.y == outro.y
        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"

v1 = Vetor(1, 2)
v2 = Vetor(3, 4)
print(v1 + v2)
print(v1 - v2)
print(v1 == v2)
print(v1)
print([v1, v2])
print(Vetor(1, 2) + 5)


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex05.py.
# ============================================================
# (4, 6)
# (-2, -2)
# False
# (1, 2)
# [Vetor(1, 2), Vetor(3, 4)]
# Traceback (most recent call last):
# TypeError: unsupported operand type(s) for +: 'Vetor' and 'int'