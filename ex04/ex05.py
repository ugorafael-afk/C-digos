# Aula 04 · Exercício 05 (casa, OBRIGATÓRIO): cadastro com idade digitada
#
# Parte 1. Classe Pessoa: o __init__ recebe nome e idade e faz
# self.idade = idade (assim o setter roda na criação).
# Escreva a property idade e o setter: só aceita de 0 a 130 (os dois valem).
# Fora disso, LEVANTE ValueError("idade precisa estar entre 0 e 130").
# Valide antes de guardar em self._idade.
# __str__   RETORNA, por exemplo:  Ana, 25 anos
# __repr__  RETORNA, por exemplo:  Pessoa('Ana', 25)
#
# Parte 2. Função cadastrar(nome, texto_idade): converte o texto com int()
# e RETORNA uma Pessoa nova. Não use try dentro dela: se o texto não for
# número, o int() já levanta ValueError; se a idade for inválida, o setter
# levanta. A função deixa o erro subir para quem chamou.
#
# Parte 3. No fim do arquivo, percorra esta lista com um for:
#     textos = ["25", "vinte", "-3", "130", "200"]
# Para cada texto, chame cadastrar("Ana", texto) dentro de um try.
#   Deu certo: mostre a pessoa com print, por exemplo:  cadastrada: Ana, 25 anos
#   e guarde ela numa lista de cadastradas (append).
#   Deu ValueError: mostre  recusado:  e a mensagem do erro
# Repare: um único except ValueError pega os dois problemas (texto que não
# é número e idade fora da faixa). No fim, mostre quantas pessoas foram
# cadastradas (para essa lista, são 2) e a própria lista com print, que usa o
# seu __repr__:  [Pessoa('Ana', 25), Pessoa('Ana', 130)]


# SE TRAVAR, REVEJA:
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   recusa no __init__ ..... aula 04, slide 21  https://poo.leoad.com.br/aulas/aula-04/#s21
#   int() de texto ......... aula 04, slide 16  https://poo.leoad.com.br/aulas/aula-04/#s16
#   o erro sobe ............ aula 04, slide 26  https://poo.leoad.com.br/aulas/aula-04/#s26
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0 or valor > 130:
            raise ValueError("idade precisa estar entre 0 e 130")
        self._idade = valor

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Pessoa '{self.nome}', {self.idade}"

def cadastrar(nome, texto_idade):
    idade = int(texto_idade)
    return nome / idade
    
textos = ["25", "vinte", "-3", "130", "200"]
cadastradas = 0
for texto in textos:
    try:
        idade_int = int(texto)
        p = Pessoa("Teste", idade_int)
        cadastradas += 1
        print(f"Sucesso: {p}")
    except ValueError as erro:
        print(f"Texto '{texto}' | Titulo Recusado:", erro)

p1 = Pessoa("ugo", 18)
p2 = Pessoa("Manu", 15)


print(str(p1))
print(repr(p2))
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# Sucesso: Teste, 25 anos
# Texto 'vinte' | Titulo Recusado: invalid literal for int() with base 10: 'vinte'
# Texto '-3' | Titulo Recusado: idade precisa estar entre 0 e 130
# Sucesso: Teste, 130 anos
# Texto '200' | Titulo Recusado: idade precisa estar entre 0 e 130
# ugo, 18 anos
# Pessoa 'Manu', 15