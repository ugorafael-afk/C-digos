# Aula 10 · Exercício 08 (casa, desafio): o cardápio e o pedido com desconto
#
# Crie a classe Prato: o __init__ recebe codigo, nome e preco.
#   __repr__  retorna, por exemplo: Prato('P3', 'Galinhada', 32)
#
# Crie a classe Cardapio, um repositório de pratos num dicionário (a chave é
# o código). O dicionário nasce vazio no __init__.
#   adicionar(prato)   guarda o prato.
#   buscar(codigo)     RETORNA o prato, ou None.
#   existe(codigo)     RETORNA True se o código está no cardápio, senão False.
#
# Crie três regras de desconto. Cada uma recebe um valor e RETORNA o valor final:
#   sem_desconto(valor)    retorna o valor sem mudar nada.
#   dez_por_cento(valor)   retorna valor * 0.9.
#   menos_cinco(valor)     retorna valor - 5, mas nunca menos que 0.
#
# Crie a classe Pedido:
#   __init__(cardapio, regra)  guarda o cardápio e a regra (uma FUNÇÃO), e
#                              cria self.codigos como uma lista vazia.
#   pedir(codigo)   acrescenta o código na lista. Se o código não existir no
#                   cardápio, levanta ValueError: código não existe no cardápio: P9
#   subtotal()      RETORNA a soma dos preços dos pratos pedidos (sum com uma
#                   comprehension que busca cada código no cardápio).
#   total()         chama a regra guardada com o subtotal e RETORNA o resultado.
#   mais_caro()     RETORNA o PRATO mais caro do pedido (max com key).
#
# Exemplo: cardápio com Prato("P1", "Pamonha", 12), Prato("P2", "Pastel", 9) e
# Prato("P3", "Galinhada", 32); pedido = Pedido(cardapio, dez_por_cento);
# pedir("P1"), pedir("P3"), pedir("P2"):
#   subtotal()    retorna 53
#   total()       retorna 47.7
#   mais_caro()   retorna Prato('P3', 'Galinhada', 32)
# Depois de pedido.regra = menos_cinco, total() retorna 48.
# pedir("P9") levanta ValueError: código não existe no cardápio: P9
#
# Teste você mesmo: no fim do arquivo, monte o cardápio e o pedido, mostre os
# resultados com print e use try/except para mostrar o erro do código P9.
#
# SE TRAVAR, REVEJA:
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   função em atributo ..... aula 10, slide 12  https://poo.leoad.com.br/aulas/aula-10/#s12
#   comprehension .......... aula 10, slide 27  https://poo.leoad.com.br/aulas/aula-10/#s27
#   sum .................... aula 10, slide 28  https://poo.leoad.com.br/aulas/aula-10/#s28
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26

class Prato:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    
    def __repr__(self):
        return f"Prato ('{self.codigo}', '{self.nome}', {self.preco})"

class Cardapio:
    def __init__(self):
        self._pratos = {}

    def adicionar(self, prato):
        self._pratos[prato.codigo] = prato

    def buscar(self, codigo):
        return self._pratos.get(codigo)

    def existe(self, codigo):
        return codigo in self._pratos

class Pedido:
    def __init__(self, cardapio, regra):
        self.cardapio = cardapio
        self.regra = regra
        self.codigo = []

    def pedir(self, codigo):
        if not self.cardapio.existe(codigo):
            raise ValueError(f"código não existe no cardápio: {codigo}")
        self.codigo.append(codigo)

    def subtotal(self): 
        return sum(comprehension.preco for codigo in self.codigo if (comprehension := self.cardapio.buscar(codigo)))

    def total(self):
        return self.regra(self.subtotal())

    def mais_caro(self):
        return max((self.cardapio.buscar(codigo) for codigo in self.codigo), key=lambda prato: prato.preco)

def sem_desconto(valor):
    return valor

def dez_por_cento(valor):
    return valor * 0.9

def menos_cinco(valor):
    return max(0, valor - 5)


lista = [Prato("P1", "Pamonha", 12), Prato("P2", "Pastel", 9), Prato("P3", "Galinhada", 32)]

cardapio = Cardapio()
p1 = Pedido(cardapio, dez_por_cento)

for p in lista:
    cardapio.adicionar(p)
p1.pedir("P1")
p1.pedir("P3")
print(p1.subtotal())
print(p1.total())
print(p1.mais_caro())
print(p1.total())
try:
    p1.pedir("P9")
except ValueError as erro:
    print(erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# 44
# 39.6
# Prato ('P3', 'Galinhada', 32)
# 39
# código não existe no cardápio: P9