# Aula 07 · Exercício 08 (casa, desafio): a classe Fracao
#
# O __init__ recebe numerador e denominador e guarda a fração já SIMPLIFICADA:
# Fracao(2, 4) guarda 1 e 2. Para simplificar, divida os dois (com //) pelo mdc.
# Denominador 0 é recusado logo no começo do __init__:
#     raise ValueError("denominador não pode ser zero")
# numerador e denominador: @property SÓ DE LEITURA (guarde em self._numerador
# e self._denominador): a fração não muda depois de criada.
# de_texto  @classmethod: recebe "3/4" e RETORNA Fracao(3, 4) (use split("/")
#           e int()). Fracao.de_texto("2/4") dá 1/2.
# Escreva a função mdc(a, b) fora da classe, com while:
#   enquanto b for diferente de 0:  resto = a % b,  depois a = b,  depois b = resto.
#   No fim, o mdc é o a.  Exemplo: mdc(2, 4) dá 2, mdc(6, 9) dá 3.
# __add__   Fracao(1, 2) + Fracao(1, 3) dá 5/6
#           (numerador: a*d + c*b;  denominador: b*d, para a/b + c/d)
# __mul__   Fracao(2, 3) * Fracao(3, 4) dá 1/2
# __eq__    Fracao(1, 2) == Fracao(3, 6) dá True, e Fracao(1, 2) == 0.5 dá False
# __lt__    Fracao(1, 3) < Fracao(1, 2) dá True   (a/b < c/d quando a*d < c*b)
# __str__   retorna, por exemplo:  1/2
# __repr__  retorna, por exemplo:  Fracao(1, 2)
# Os operadores RETORNAM uma Fracao NOVA (ou True/False) e não mudam o self.
# Se o outro não for Fracao, retorne NotImplemented.
#
# Teste você mesmo: no fim do arquivo, crie as frações e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que Fracao(1, 0) é recusada.
#
# SE TRAVAR, REVEJA:
#   __add__ ................ aula 07, slide 25  https://poo.leoad.com.br/aulas/aula-07/#s25
#   NotImplemented ......... aula 07, slide 30  https://poo.leoad.com.br/aulas/aula-07/#s30
#   __lt__ e __len__ ....... aula 07, slide 36  https://poo.leoad.com.br/aulas/aula-07/#s36
#   recusa no __init__ ..... aula 04, slide 21  https://poo.leoad.com.br/aulas/aula-04/#s21
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("denominador não pode ser zero")
        m = mdc(numerador, denominador)
        self._numerador = numerador // m
        self._denominador = denominador // m

    @property
    def numerador(self):
        return self._numerador
    @property
    def denominador(self):
        return self._denominador
    
    @classmethod
    def de_texto(cls, texto):
        n, d = map(int, texto.split("/"))
        return cls(n, d)

    def __add__(self, outro):
        if isinstance(outro, Fracao):
            n = self.numerador * outro.denominador + outro.numerador * self.denominador
            d = self.denominador * outro.denominador
            return Fracao(n, d)
        return NotImplemented

    def __mul__(self, outro):
        if isinstance(outro, Fracao):
            n = self.numerador * outro.numerador
            d = self.denominador * outro.denominador
            return Fracao(n, d)
        return NotImplemented

    def __eq__(self, outro):
        if isinstance(outro, Fracao):
            return self.numerador == outro.numerador and self.denominador == outro.denominador
        return NotImplemented

    def __lt__(self, outro):
        if isinstance(outro, Fracao):
            return self.numerador * outro.denominador < outro.numerador * self.denominador
        return NotImplemented

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self):
        return f"Fracao({self.numerador}, {self.denominador})"

def mdc(a, d):
    while d != 0:
        resto = a % d
        a = d
        d = resto
    return a

f1 = Fracao(1, 2)
f2 = Fracao(1, 3)
print(f1 + f2)
print(f1 * f2)
print(f1 == Fracao(2, 4))
print(f1 < f2)
try:
    f3 = Fracao(1, 0)
except ValueError as erro:
    print(erro)
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# 5/6
# 1/6
# True
# False
# denominador não pode ser zero