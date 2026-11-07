# Aula 09 · Exercício 05 (casa, OBRIGATÓRIO): imóveis para alugar
#
# Escreva as classes do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex05-imovel.svg
# Imovel é abstrata: herda de ABC, e aluguel() é ABSTRATO.
#   __str__     RETORNA, por exemplo:  Rua 10, 80 m²: R$ 1900.00
#               (use self.aluguel() e :.2f)
# Casa          o __init__ recebe endereco, area e quintal (True ou False).
#   aluguel()   20 por m², mais 300 se tiver quintal.
# Apartamento   o __init__ recebe endereco, area e condominio.
#   aluguel()   25 por m², mais o condomínio.
# As duas filhas chamam super().__init__(endereco, area).
#
# Exemplos:
#   Casa("Rua 10", 80, True)              Rua 10, 80 m²: R$ 1900.00
#   Apartamento("Av. T-63", 60, 450)      Av. T-63, 60 m²: R$ 1950.00
#
# Por fim, mostre que o Imovel genérico é recusado: dentro de um
# try/except TypeError, tente criar Imovel("Rua 1", 50) e, no except,
# imprima Imovel recusado.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   o triângulo ............ aula 09, slide 21  https://poo.leoad.com.br/aulas/aula-09/#s21
#   «abstract» ............. aula 09, slide 27  https://poo.leoad.com.br/aulas/aula-09/#s27
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8

from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, endereco, area):
        self.endereco = endereco
        self.area = area

    @abstractmethod
    def aluguel(self):
        pass

    def __str__(self):
        return f"{self.endereco}, {self.area} m²: R$ {self.aluguel():.2f}"

class Casa(Imovel):
    def __init__(self, endereco, area, quintal):
        super().__init__(endereco, area)
        self.quintal = quintal

    def aluguel(self):
        return 20 * self.area + (300 if self.quintal else 0)

class Apartamento(Imovel):
    def __init__(self, endereco, area, condominio):
        super().__init__(endereco, area)
        self.condominio = condominio

    def aluguel(self):
        return 25 * self.area + self.condominio

c1 = Casa("Rua 10", 80, True)
a1 = Apartamento("Av. T-63", 60, 450)

print(c1)
print(a1)

try:
    i1 = Imovel("Rua 1", 50)
except TypeError:
    print("Imovel recusado")
        


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# Rua 10, 80 m²: R$ 1900.00
# Av. T-63, 60 m²: R$ 1950.00
# Imovel recusado