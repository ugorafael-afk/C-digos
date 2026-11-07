# Aula 10 · Exercício 04 (casa, OBRIGATÓRIO): filtrar com uma regra
#
# Crie três funções. Cada uma recebe um número e RETORNA True ou False:
#   eh_par(n)        True se n for par (n % 2 == 0).
#   eh_positivo(n)   True se n for maior que zero.
#   eh_grande(n)     True se n for maior que 10.
#
# Crie a função filtrar(numeros, regra). Ela RETORNA uma lista NOVA só com os
# números para os quais regra(numero) dá True. Use for, if e append.
# A regra chega como valor, sem parênteses: filtrar(numeros, eh_par).
#
# Exemplos, com numeros = [3, -2, 8, 15, -7, 10]:
#   filtrar(numeros, eh_par)             retorna [-2, 8, 10]
#   filtrar(numeros, eh_positivo)        retorna [3, 8, 15, 10]
#   filtrar(numeros, eh_grande)          retorna [15]
#   filtrar([], eh_par)                  retorna []
#
# Teste você mesmo: no fim do arquivo, chame filtrar com cada regra e mostre
# os resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   f × f() ................ aula 10, slide 8  https://poo.leoad.com.br/aulas/aula-10/#s8
#   função como argumento .. aula 10, slide 11  https://poo.leoad.com.br/aulas/aula-10/#s11

def eh_par(n):
    return n % 2 == 0

def eh_positivo(n):
    return n > 0
    
def eh_grande(n):
    return n > 10

def filtrar(numeros, regras):
    resultados = []
    for numero in numeros:
        if regras(numero):
            resultados.append(numero)
    return resultados

lista = [3, -2, 8, 15, -7, 10]
print(filtrar(lista, eh_par))
print(filtrar(lista, eh_positivo))
print(filtrar(lista, eh_grande))
print(filtrar([], eh_par))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
