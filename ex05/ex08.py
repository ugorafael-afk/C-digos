# Aula 05 · Exercício 08 (casa, desafio): o pedido completo da lanchonete
#
# Cliente: o __init__ recebe nome.
# Produto: o __init__ recebe nome e preco.
#   preco  @property e @preco.setter. O setter RECUSA preço negativo:
#              raise ValueError("preço não pode ser negativo")
#   de_texto(texto)  construtor alternativo, com @classmethod: recebe "Pastel;8"
#                    e RETORNA cls(nome, preco), com o preço convertido por float().
# ItemPedido: o __init__ recebe produto (um Produto) e quantidade.
#   subtotal()  RETORNA o preço do produto vezes a quantidade.
# Pedido:
#   atributos de CLASSE: taxa_entrega = 6 e total_pedidos = 0.
#   o __init__ recebe cliente (um Cliente JÁ CRIADO: associação), cria
#     self.itens como lista vazia e soma 1 em Pedido.total_pedidos.
#   adicionar(produto, quantidade)  CRIA o ItemPedido ali dentro (composição).
#   subtotal()  RETORNA a soma dos subtotais dos itens, usando um for.
#   total()     RETORNA o subtotal mais a taxa de entrega. Com subtotal de 50
#               ou mais, a entrega é grátis.
#   __str__     retorna, por exemplo: Pedido de Ana: 2 itens, total R$ 28.50
#               (o total sempre com 2 casas decimais: :.2f)
#
# Exemplos:
#   ana = Cliente("Ana")
#   pastel = Produto.de_texto("Pastel;8")
#   caldo = Produto.de_texto("Caldo de cana;6.5")
#   Pedido(ana) com 2 pastéis e 1 caldo: subtotal() 22.5, total() 28.5,
#   e o print do pedido mostra Pedido de Ana: 2 itens, total R$ 28.50
#   Pedido(ana) com 7 pastéis: total() 56.0 (entrega grátis).
#   Depois de Pedido.taxa_entrega = 8, o primeiro pedido passa a ter total() 30.5.
#   Depois desses dois pedidos, Pedido.total_pedidos vale 2.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   composição ............. aula 05, slide 38  https://poo.leoad.com.br/aulas/aula-05/#s38
#   associação ............. aula 05, slide 39  https://poo.leoad.com.br/aulas/aula-05/#s39
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("preço não pode ser negativo")
        self._preco = valor

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], float(partes[1]))

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido :
    taxa_entrega = 6
    total_pedidos = 0

    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        Pedido.total_pedidos += 1

    def adicionar(self, produto, quantidade):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)

    def subtotal(self):
        total = 0
        for item in self.itens:
            total += item.subtotal()
        return total

    def total(self):
        subtotal = self.subtotal()
        if subtotal >= 50:
            return subtotal
        else:
            return subtotal + Pedido.taxa_entrega

    def __str__(self):
        return f"Pedido de {self.cliente.nome}: {len(self.itens)} itens, total R$ {self.total():.2f}"

c1 = Cliente("Ana")
p1 = Produto.de_texto("Pastel;8")
p2 = Produto.de_texto("Caldo de cana;6.5")
pedido1 = Pedido(c1)
pedido1.adicionar(p1, 2)
pedido1.adicionar(p2, 1)
print(pedido1.subtotal())
print(pedido1.total())
pedido2 = Pedido(c1)
pedido2.adicionar(p1, 7)
print(pedido2.total())
Pedido.taxa_entrega = 8
print(pedido1.total())
print(Pedido.total_pedidos)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# 22.5
# 28.5
# 56.0
# 30.5
# 2