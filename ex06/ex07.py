# Aula 06 · Exercício 07 (casa, opcional): o produto perecível
#
# Produto: o __init__ recebe nome e preco.
#   preco          @property e @preco.setter. O setter RECUSA preço negativo:
#                      raise ValueError("preço negativo")
#                  O __init__ faz self.preco = preco: o setter roda na criação.
#   preco_final()  RETORNA o preco.
#   __str__        retorna, por exemplo:  Queijo: R$ 30.00
#                  (use self.preco_final() no texto)
#
# Perecivel é um Produto com dias de validade:
#   o __init__ recebe nome, preco e dias.
#     Se dias for menor que 1, faça raise ValueError("produto vencido") ANTES do super().
#     Depois, super().__init__ para nome e preco, e guarde os dias.
#   preco_final()  com 2 dias ou menos, RETORNA o preço do pai (super()) com 30% de
#                  desconto; senão, RETORNA o preço do pai sem desconto.
#   Exemplos: Perecivel("Iogurte", 10, 2) aparece como  Iogurte: R$ 7.00
#             Perecivel("Queijo", 30, 10) aparece como  Queijo: R$ 30.00
#
# Teste você mesmo: no fim do arquivo, mostre os exemplos com print e use
# try/except para mostrar que Perecivel("Leite", -5, 3) e Perecivel("Pão", 8, 0)
# são recusados, cada um com a sua mensagem.
#
# SE TRAVAR, REVEJA:
#   raise antes do super() . aula 06, slide 20  https://poo.leoad.com.br/aulas/aula-06/#s20
#   substituir × estender .. aula 06, slide 25  https://poo.leoad.com.br/aulas/aula-06/#s25
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   except ... as erro ..... aula 04, slide 15  https://poo.leoad.com.br/aulas/aula-04/#s15
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preço negativo")
        self._preco = valor

    def preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.nome}: R$ {self.preco_final():.2f}"

class Perecivel(Produto):
    def __init__(self, nome, preco, dias):
        if dias < 1:
            raise ValueError("produto Vencido")
        super().__init__(nome, preco)
        self.dias = dias 


    def preco_final(self):
        if self.dias <= 2:
            return super().preco_final() * 0.7
        else:
            return super().preco_final()

p1 = Perecivel("Iogurte", 10, 2)
p2 = Perecivel("Queijo", 30, 10)
print(str(p1))
print(str(p2))
try:
    p3 = Perecivel("Leite", -5, 3)
except ValueError:
    print("Preço negativo, não valido")
try:
    p4 = Perecivel("Pão", 8, 0)
except ValueError:
    print("Produto vencido, não valido")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# Iogurte: R$ 7.00
# Queijo: R$ 30.00
# Preço negativo, não valido
# Produto vencido, não valido
