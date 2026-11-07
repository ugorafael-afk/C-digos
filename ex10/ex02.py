# Aula 10 · Exercício 02 (casa, OBRIGATÓRIO): o ranking dos jogadores
#
# A classe Jogador já está pronta. Crie as funções abaixo. Todas RETORNAM,
# nenhuma imprime, e nenhuma muda a lista que recebeu.
#   pegar_pontos(jogador)    retorna os pontos do jogador.
#   ranking(jogadores)       retorna uma lista NOVA, do maior para o menor em
#                            pontos. Use sorted com key=pegar_pontos e reverse=True.
#   campeao(jogadores)       retorna o JOGADOR (o objeto) com mais pontos.
#                            Use max com key=pegar_pontos.
#   lanterna(jogadores)      retorna o JOGADOR com menos pontos.
#                            Use min com key=lambda.
#   total_pontos(jogadores)  retorna a soma dos pontos de todos.
#                            Use sum com uma comprehension.
#
# SE TRAVAR, REVEJA:
#   sorted com key ......... aula 10, slide 19  https://poo.leoad.com.br/aulas/aula-10/#s19
#   reverse=True ........... aula 10, slide 22  https://poo.leoad.com.br/aulas/aula-10/#s22
#   sorted × .sort() ....... aula 10, slide 23  https://poo.leoad.com.br/aulas/aula-10/#s23
#   lambda ................. aula 10, slide 24  https://poo.leoad.com.br/aulas/aula-10/#s24
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26
#   comprehension .......... aula 10, slide 27  https://poo.leoad.com.br/aulas/aula-10/#s27
#   sum .................... aula 10, slide 28  https://poo.leoad.com.br/aulas/aula-10/#s28

class Jogador:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def __repr__(self):
        return f"Jogador('{self.nome}', {self.pontos})"
    
def pegar_pontos(jogador):
    return jogador.pontos
    
def ranking(jogadores):
    return sorted(jogadores, key=pegar_pontos, reverse=True)
    
def campeao(jogadores):
    return max(jogadores, key=pegar_pontos)
    
def lanterna(jogadores):
    return min(jogadores, key=lambda jogador: jogador.pontos)
    
def total_pontos(jogadores):
    return sum(pegar_pontos(jogador) for jogador in jogadores)


# ===== TESTE (não altere estas linhas) =====
jogadores = [Jogador("Ana", 120), Jogador("Duda", 80), Jogador("Caio", 150), Jogador("Bruno", 95)]

print(ranking(jogadores))         # [Jogador('Caio', 150), Jogador('Ana', 120), Jogador('Bruno', 95), Jogador('Duda', 80)]
print(jogadores[0])               # Jogador('Ana', 120)
print(campeao(jogadores))         # Jogador('Caio', 150)
print(lanterna(jogadores).nome)   # Duda
print(total_pontos(jogadores))    # 445

print(f"chave: {ranking(jogadores)[1].nome}-{campeao(jogadores).nome}-{lanterna(jogadores).pontos}-{total_pontos(jogadores)}-{jogadores[0].nome}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
