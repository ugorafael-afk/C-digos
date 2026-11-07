# Aula 08 · Exercício 06 (casa, opcional): formas com área e perímetro
#
# Crie a classe abstrata Forma (herda de ABC):
#   __init__(nome)   guarda o nome.
#   area()           método ABSTRATO.
#   perimetro()      método ABSTRATO.
#   __str__          concreto: retorna, por exemplo:
#                    Retângulo: área 12, perímetro 14
#
# Cada filha também escreve o seu __repr__, que parece a linha que cria o
# objeto: Retangulo(4, 3) e Circulo(1).
#
# E as duas filhas (cada uma chama super().__init__ com o próprio nome):
# Retangulo(largura, altura)   área = largura * altura
#                              perímetro = 2 * (largura + altura)
# Circulo(raio)                área = 3.14 * raio * raio
#                              perímetro = 2 * 3.14 * raio
#
# Depois, fora das classes, a função maior_area(formas): recebe uma lista
# de formas e RETORNA a forma de maior área, usando um for. Lista vazia
# retorna None.
#
# Exemplos:
#   print(Retangulo(4, 3))   Retângulo: área 12, perímetro 14
#   print(Circulo(1))        Círculo: área 3.14, perímetro 6.28
#   print(maior_area([Retangulo(4, 3), Circulo(2), Retangulo(1, 1)]))
#                            Círculo: área 12.56, perímetro 12.56
#   print(maior_area([]))    None
#   print([Retangulo(4, 3), Circulo(1)])   [Retangulo(4, 3), Circulo(1)]
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   mais de um abstrato .... aula 08, slide 15  https://poo.leoad.com.br/aulas/aula-08/#s15
#   abstrato e concreto .... aula 08, slide 13  https://poo.leoad.com.br/aulas/aula-08/#s13
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return f"{self.nome}: Area {self.area()}, perímetro {self.perimetro()}"

class Retangulo(Forma):
    def __init__(self, nome, largura, altura):
        super().__init__(nome)
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.altura + self.largura)

    def __repr__(self):
        return f"Retangulo({self.largura}, {self.altura})"

class Circulo(Forma):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def __repr__(self):
        return f"Circulo({self.raio})"

def maior_area(formas):
    if not formas:
        return None
    maior = formas[0]
    for forma in formas:
        if forma.area() > maior.area():
            maior = forma
    return maior

print(Retangulo("Retângulo", 4, 3))
print(Circulo("Círculo", 1))
formas = [Retangulo("Retângulo", 4, 3), Circulo("Círculo", 2), Retangulo("Retângulo", 1, 1)]
print(maior_area(formas))
print(maior_area([]))
print([Retangulo("Retângulo", 4, 3), Circulo("Círculo", 1)])

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# Retângulo: Area 12, perímetro 14
# Círculo: Area 3.14, perímetro 6.28
# Círculo: Area 12.56, perímetro 12.56
# None
# [Retangulo(4, 3), Circulo(1)]