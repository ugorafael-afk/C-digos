# Aula 01 · Exercício 04 (casa, OBRIGATÓRIO): apresentação
#
# Crie a função apresentacao(nome, idade, cidade="Anápolis"), que DEVOLVE o texto:
#   Olá! Meu nome é <nome>, tenho <idade> anos e moro em <cidade>.
#
def __init__(self, nome, idade, cidade="Anápolis"):
    self.nome = nome
    self.idade = idade
    self.cidade = cidade

def apresentacao(nome, idade, cidade="Anápolis"):
    return f"Olá! Meu nome é {nome}, tenho {idade} anos e moro em {cidade}."

print(apresentacao("Ana", 22))

# No fim do seu código, teste a sua função com print. Por exemplo:
#   print(apresentacao("Ana", 22))
#   print(apresentacao("Bruno", 19, "Goiânia"))


# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-01. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA: Olá! Meu nome é Ana, tenho 22 anos e moro em Anápolis.