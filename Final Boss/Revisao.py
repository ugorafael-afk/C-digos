# 1ª VA · Treino 1: a comanda da cafeteria
#
# Escreva a classe ItemPedido, um item da comanda:
# - o __init__ recebe nome, preco e quantidade e guarda os três;
# - total() RETORNA o preço vezes a quantidade;
# - __str__ RETORNA o texto do item, por exemplo:
#       2x Café coado: R$ 12.00
#   (a quantidade, um x, o nome e o total com 2 casas decimais)
# Nenhum print dentro da classe.


class ItemPedido:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def total(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.nome}: R$ {self.total():.2f}"

# ===== TESTE (não altere estas linhas) =====
cafe = ItemPedido("Café coado", 6, 2)
pao = ItemPedido("Pão de queijo", 4.5, 3)

print(cafe.total())     # 12
print(pao.total())      # 13.5
print(cafe)             # 2x Café coado: R$ 12.00
print(pao)              # 3x Pão de queijo: R$ 13.50

conta = 0
for item in [cafe, pao, ItemPedido("Suco", 9, 1)]:
    conta = conta + item.total()
print(f"Conta: R$ {conta:.2f}")    # Conta: R$ 34.50