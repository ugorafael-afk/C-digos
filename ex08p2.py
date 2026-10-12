# Aula 02 · Exercício 08 (casa, desafio): Pizza e Carrinho
#
# Pizza: o __init__ recebe sabor e preco. Só __repr__: Pizza('Calabresa', 45)
# Carrinho: nasce com self.pizzas = [] (lista vazia).
#   adicionar(pizza)  coloca a pizza na lista.
#   total()           RETORNA a soma dos preços, usando um for.
#   mais_cara()       RETORNA o objeto Pizza mais caro, usando um for.
#                     Se o carrinho estiver vazio, retorna None.
#   __str__           retorna, por exemplo: Carrinho: 3 pizzas, total R$ 132.50
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class Pizza:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco

    def __repr__(self):
        return f"Pizza('{self.sabor}', {self.preco})"

class Carrinho:
    def __init__(self):
        self.pizzas = []

    def adicionar(self, pizza):
        self.pizzas.append(pizza)

    def total(self):
        total_preco = 0
        for pizza in self.pizzas:
            total_preco += pizza.preco
        return total_preco

    def mais_cara(self):
        if not self.pizzas:
            return None
        mais_cara_pizza = self.pizzas[0]
        for pizza in self.pizzas:
            if pizza.preco > mais_cara_pizza.preco:
                mais_cara_pizza = pizza
        return mais_cara_pizza

    def __str__(self):
        return f"Carrinho: {len(self.pizzas)} pizzas, total R$ {self.total():.2f}"

pizza1 = Pizza('Calabresa', 45)
pizza2 = Pizza('Margherita', 40)
carrinho = Carrinho()
carrinho.adicionar(pizza1)
carrinho.adicionar(pizza2)
print(carrinho)
print(carrinho.total())
print(carrinho.mais_cara())
print(repr(pizza1))
print(repr(pizza2))


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
