# Aula 01 · Exercício 08 (casa, desafio): triângulo
#
# Crie a função tipo_triangulo(a, b, c), que DEVOLVE:
#   "Não é triângulo" se algum lado for maior ou igual à soma dos outros dois;
#   "Equilátero" se os 3 lados forem iguais;
#   "Isósceles" se exatamente 2 lados forem iguais;
#   "Escaleno" se os 3 forem diferentes.
#
# No fim do seu código, teste a sua função com print. Por exemplo:
#   print(tipo_triangulo(3, 4, 5))
#   print(tipo_triangulo(1, 2, 10))

def tipo_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "Não é triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


print(tipo_triangulo(3, 4, 5))
print(tipo_triangulo(1, 2, 10))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
