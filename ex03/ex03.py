# Aula 03 · Exercício 03 (sala): proteger o Produto sem mudar quem usa
#
# A classe Produto abaixo JÁ RODA, mas não protege nada: aceita estoque
# negativo. Proteja a classe POR DENTRO. O teste é o código de quem usa:
# ele não muda.
# nome              @property só de leitura (guarde em self._nome).
# estoque           @property com setter que CORRIGE: abaixo de 0 vira 0.
#                   Guarde em self._estoque.
# valor_em_estoque  @property calculada: RETORNA preço vezes estoque.
# O preço fica público, como está (self.preco): neste exercício, sem regra.
# vender e repor ficam como estão: com o estoque virando property, eles
# passam a usar o setter sozinhos.


class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self.preco = preco
        self.estoque = estoque

    @property
    def nome (self):
        return self._nome
    
    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            valor = 0
        self._estoque = valor

    @property
    def valor_em_estoque(self):
        return self.preco * self.estoque

    def vender(self, quantidade):
        self.estoque = self.estoque - quantidade

    def repor(self, quantidade):
        self.estoque = self.estoque + quantidade


# ===== TESTE (não altere estas linhas) =====
p1 = Produto("Caderno", 25, 10)
p2 = Produto("Caneta", 3, -4)              # estoque negativo vira 0

print(p1.nome, p1.preco, p1.estoque)       # Caderno 25 10
print(p2.nome, p2.estoque)                 # Caneta 0

p1.vender(3)
print(p1.estoque, p1.valor_em_estoque)     # 7 175
p1.vender(20)                              # vendeu mais do que tinha
print(p1.estoque, p1.valor_em_estoque)     # 0 0

p2.repor(5)
p2.preco = 4
print(p2.estoque, p2.valor_em_estoque)     # 5 20

# Só o teste olha por dentro, para conferir que você guardou com _:
print(p1._nome, p1._estoque)               # Caderno 0

print(f"chave: {p2.nome}-{p1._estoque}-{p2.estoque}-{p2.valor_em_estoque}-{Produto('Lápis', 2, -1).estoque}-{Produto('Borracha', 1, 6).valor_em_estoque}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
