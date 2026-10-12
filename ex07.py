# Aula 01 · Exercício 07 (casa, opcional): o maior da lista
#
# Crie a função maior(numeros), que DEVOLVE o maior número da lista, SEM usar max().
# Dica: comece guardando o primeiro item (numeros[0]) e passe pela lista com for e if.
#
# No fim do seu código, teste a sua função com print. Por exemplo:
#   print(maior([4, 17, 9]))
#   print(maior([-5, -2, -9]))

def maior(numeros):
    maior = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
    return maior

print(maior([4, 17, 9]))
print(maior([-5, -2, -9]))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA: 17 -2
