# Aula 02 · Exercício 05 (casa, OBRIGATÓRIO): a classe Retangulo
# O __init__ recebe largura e altura.
# area()          RETORNA largura vezes altura.
# perimetro()     RETORNA 2 vezes (largura + altura).
# eh_quadrado()   RETORNA True se largura e altura forem iguais, senão False.
# __str__         retorna, por exemplo: Retângulo 4x3 | área 12 | perímetro 14
#                 (use self.area() e self.perimetro())
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.



class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def eh_quadrado(self):
        return self.largura == self.altura

    def __str__(self):
        return f"Retângulo {self.largura}x{self.altura} | área {self.area()} | perímetro {self.perimetro()}"

retangulo1 = Retangulo(4, 3)
retangulo2 = Retangulo(5, 5)

print(retangulo1)
print(retangulo2)


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA: Retângulo 4x3 | área 12 | perímetro 14 Retângulo 5x5 | área 25 | perímetro 20