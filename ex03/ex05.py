# Aula 03 · Exercício 05 (casa, OBRIGATÓRIO): a caixa d'água
#
# Classe CaixaDagua. O __init__ recebe capacidade (em litros) e a caixa
# nasce vazia. Guarde a capacidade ANTES de mexer nos litros.
# capacidade   @property só de leitura.
# litros       @property com setter que CORRIGE: abaixo de 0 vira 0;
#              acima da capacidade vira a capacidade.
# encher(quantidade)   soma litros, passando pelo setter (self.litros = ...).
# gastar(quantidade)   tira litros, passando pelo setter.
# porcentagem  @property calculada: RETORNA litros * 100 / capacidade
# __str__      retorna, por exemplo: Caixa: 750 de 1000 litros (75.0%)
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Encha além da capacidade e gaste mais do que tem,
# para ver o setter corrigindo.

class CaixaDagua:
    def __init__(self, capacidade):
        self._capacidade = capacidade
        self.litros = 0

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def litros(self):
        return self._litros

    @litros.setter
    def litros(self, valor):
        if valor < 0:
            valor = 0
        elif valor > self.capacidade:
            valor = self.capacidade
        self._litros = valor

    def encher(self, quantidade):
        self.litros = self.litros + quantidade

    def gastar(self, quantidade):
        self.litros = self.litros - quantidade

    @property
    def porcentagem(self):
        return self.litros * 100 / self.capacidade

    def __str__(self):
        return f"Caixa: {self.litros} de {self.capacidade} litros ({self.porcentagem:.1f}%)"

c1 = CaixaDagua(1000)
c2 = CaixaDagua(500)

print(c1)
c1.encher(750)
print(c1)
c1.encher(500)
print(c1)
c1.gastar(200)
print(c1)
print(c2)
c2.encher(600)
print(c2)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
