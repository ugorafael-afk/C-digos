# Aula 10 · Exercício 05 (casa, OBRIGATÓRIO): os produtos da loja
#
# Crie a classe Produto. O __init__ recebe nome, preco e estoque (quantas
# unidades tem guardadas) e guarda os três.
#   __repr__  retorna, por exemplo: Produto('Caneca', 35, 12)
#
# Crie as funções abaixo. Todas RETORNAM, nenhuma imprime:
#   mais_barato(produtos)        retorna o PRODUTO (o objeto) mais barato.
#                                Use min com key=lambda.
#   por_preco(produtos)          retorna uma lista NOVA, do mais caro para o
#                                mais barato. Use sorted com key e reverse=True.
#   valor_do_estoque(produtos)   retorna a soma de preco * estoque de todos.
#                                Use sum com uma comprehension.
#   em_falta(produtos)           retorna a lista dos NOMES dos produtos com
#                                estoque 0. Use uma comprehension com if.
#
# Exemplos, com
#   produtos = [Produto("Caneca", 35, 12), Produto("Boné", 42, 0),
#               Produto("Camiseta", 59.9, 5), Produto("Chaveiro", 15, 0)]
#   mais_barato(produtos)        retorna Produto('Chaveiro', 15, 0)
#   por_preco(produtos)          retorna [Produto('Camiseta', 59.9, 5), Produto('Boné', 42, 0), Produto('Caneca', 35, 12), Produto('Chaveiro', 15, 0)]
#   valor_do_estoque(produtos)   retorna 719.5
#   em_falta(produtos)           retorna ['Boné', 'Chaveiro']
#
# Teste você mesmo: no fim do arquivo, crie a lista de produtos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26
#   sorted com key ......... aula 10, slide 19  https://poo.leoad.com.br/aulas/aula-10/#s19
#   reverse=True ........... aula 10, slide 22  https://poo.leoad.com.br/aulas/aula-10/#s22
#   comprehension .......... aula 10, slide 27  https://poo.leoad.com.br/aulas/aula-10/#s27
#   sum .................... aula 10, slide 28  https://poo.leoad.com.br/aulas/aula-10/#s28

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def __repr__(self):
        return f"Produto('{self.nome}', {self.preco}, {self.estoque})"
    
def mais_barato(produtos):
    return min(produtos, key=lambda produto: produto.preco)

def por_preco(produtos):
    return sorted(produtos, key=lambda produto: produto.preco, reverse=True)

def valor_do_estoque(produtos):
    return sum(produto.preco * produto.estoque for produto in produtos)

def em_falta(produtos):
    return [produto.nome for produto in produtos if produto.estoque == 0]

lista = [Produto("Caneca", 35, 12), Produto("Boné", 42, 0), Produto("Camiseta", 59.9, 5), Produto("Chaveiro", 15, 0)]

print(mais_barato(lista))
print(por_preco(lista))
print(valor_do_estoque(lista))
print(em_falta(lista))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
