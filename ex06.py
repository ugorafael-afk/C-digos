# Aula 01 · Exercício 06 (casa, opcional): conversor de temperatura
#
# Crie duas funções:
#   celsius_para_fahrenheit(c): DEVOLVE c * 1.8 + 32
#   converter_lista(temperaturas): DEVOLVE uma LISTA NOVA com cada valor convertido.
#
# No fim do seu código, teste a sua função com print. Por exemplo:
#   print(celsius_para_fahrenheit(25))
#   print(converter_lista([0, 25, 100]))

def celsius_para_fahrenheit(c):
    return c * 1.8 + 32

def converter_lista(temperaturas):
    return [celsius_para_fahrenheit(t) for t in temperaturas]

print(celsius_para_fahrenheit(25))
print(converter_lista([0, 25, 100]))


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA: 77.0  [32.0, 77.0, 212.0]
