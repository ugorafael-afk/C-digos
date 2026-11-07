# Aula 10 · Exercício 07 (casa, opcional): a agenda de contatos
#
# Crie a classe Contato. O __init__ recebe nome e telefone e guarda os dois.
#   __repr__  retorna, por exemplo: Contato('Ana', '62 99999-0001')
#
# Crie a classe Agenda, que guarda os contatos num dicionário (a chave é o
# nome, o valor é o objeto Contato). O dicionário nasce vazio no __init__.
#   adicionar(contato)  guarda o contato. Se o nome já existir, levanta
#                       ValueError com a mensagem: contato repetido: Ana
#   buscar(nome)        RETORNA o contato, ou None se o nome não existir.
#   remover(nome)       apaga e RETORNA True; se o nome não existir, RETORNA False.
#   listar()            RETORNA a lista dos contatos em ordem alfabética de
#                       nome. Use sorted sobre os valores, com key=lambda.
#
# Exemplo: depois de adicionar Caio, Ana e Bia, nessa ordem,
#   listar()         retorna [Contato('Ana', '62 99999-0001'), Contato('Bia', '62 99999-0002'), Contato('Caio', '62 99999-0003')]
#   buscar("Duda")   retorna None
#   remover("Caio") retorna True; chamando de novo, retorna False
#   adicionar outro contato chamado Ana: ValueError: contato repetido: Ana
#
# Teste você mesmo: no fim do arquivo, crie a agenda, mostre os resultados
# com print e use try/except para mostrar a mensagem do contato repetido.
#
# SE TRAVAR, REVEJA:
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   except ... as erro ..... aula 04, slide 15  https://poo.leoad.com.br/aulas/aula-04/#s15
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   dicionário no __init__ . aula 10, slide 42  https://poo.leoad.com.br/aulas/aula-10/#s42
#   sorted com key ......... aula 10, slide 19  https://poo.leoad.com.br/aulas/aula-10/#s19
#   lambda ................. aula 10, slide 24  https://poo.leoad.com.br/aulas/aula-10/#s24

class Contato:
    def __init__(self, nome , telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"Contato('{self.nome}', '{self.telefone}')"

class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar(self, contato):
        if contato.nome in self.contatos:
            raise ValueError(f"Contato repetido: {contato.nome}")
        self.contatos[contato.nome] = contato

    def buscar(self, nome):
        return self.contatos.get(nome, None)

    def remover(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            return True
        return False

    def lista(self):
        return sorted(self.contatos.values(), key=lambda p: p.nome)

lista = [Contato("Caio", "62 99999-0003"), Contato("Ana", "62 99999-0001"), Contato("Bia", "62 99999-0002")]

a1 = Agenda()
for c in lista:
    a1.adicionar(c)

print(a1.lista())
print(a1.buscar("Duda"))
print(a1.remover("Caio"))

try:
    a1.adicionar(Contato("Ana", "62 99999-0001"))
except ValueError as erro:
    print(erro)
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
