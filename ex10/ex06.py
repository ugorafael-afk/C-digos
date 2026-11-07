# Aula 10 · Exercício 06 (casa, opcional): o contador de votos
#
# Crie a função contar_votos(votos). Ela recebe uma lista de nomes (um nome
# por voto) e RETORNA um dicionário: a chave é o nome, o valor é quantos
# votos ele teve.
#   Dica: comece com um dicionário vazio. Para cada voto, o novo valor é o
#   valor antigo mais 1; use .get(nome, 0) para o nome que ainda não apareceu.
#
# Crie a função vencedor(contagem). Ela recebe o dicionário e RETORNA o nome
# com mais votos.
#   Dica: max sobre um dicionário passa pelas CHAVES. A key pode olhar o valor
#   de cada chave: key=lambda nome: contagem[nome]
#
# Exemplos, com votos = ["Ana", "Bia", "Ana", "Caio", "Ana", "Bia"]:
#   contar_votos(votos)              retorna {'Ana': 3, 'Bia': 2, 'Caio': 1}
#   vencedor(contar_votos(votos))    retorna 'Ana'
#   contar_votos([])                 retorna {}
#
# Teste você mesmo: no fim do arquivo, mostre os resultados com print.
#
# SE TRAVAR, REVEJA:
#   dicionário ............. aula 10, slide 33  https://poo.leoad.com.br/aulas/aula-10/#s33
#   [ ] × .get() ........... aula 10, slide 34  https://poo.leoad.com.br/aulas/aula-10/#s34
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26
#   lambda ................. aula 10, slide 24  https://poo.leoad.com.br/aulas/aula-10/#s24

def contar_votos(votos):
    contagem = {}
    for voto in votos:
        contagem[voto] = contagem.get(voto, 0) + 1
    return contagem

def vencedor(contagem):
    return max(contagem, key=lambda nome: contagem[nome])

votos = ["Ana", "Bia", "Ana", "Caio", "Ana", "Bia"]

print(contar_votos(votos))
print(vencedor(contar_votos(votos)))
print(contar_votos([]))


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
