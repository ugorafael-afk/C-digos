# Aula 09 · Exercício 04 (casa, OBRIGATÓRIO): a academia
#
# Escreva as 3 classes do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex04-academia.svg
# Leia as duas linhas: a Academia RECEBE alunos prontos (linha simples);
# o Aluno CRIA os próprios treinos (losango cheio).
#
# Treino           guarda tipo e minutos.
# Aluno            começa com a lista treinos vazia.
#   novo_treino(tipo, minutos)  cria o Treino e guarda na lista.
#   minutos()                   RETORNA a soma dos minutos dos treinos.
# Academia         começa com a lista alunos vazia.
#   matricular(aluno)           guarda o aluno recebido.
#   minutos_totais()            RETORNA a soma de minutos() de todos os alunos.
#
# Exemplo: a Ana faz musculação 60 min e esteira 30 min; o Bruno faz
# natação 45 min. Os dois matriculados: minutos_totais() dá 135.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print.
#
# SE TRAVAR, REVEJA:
#   linhas do diagrama ..... aula 09, slide 15  https://poo.leoad.com.br/aulas/aula-09/#s15
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42

class Treino:
    def __init__(self, tipo, minutos):
        self.tipo = tipo
        self.minutos = minutos

class Aluno:
    def __init__(self):
        self.treinos = []

    def novo_treino(self, tipo, minutos):
        treino = Treino(tipo, minutos)
        self.treinos.append(treino)

    def minutos(self):
        return sum(treino.minutos for treino in self.treinos)

class Academia:

    def __init__(self):
        self.alunos = []

    def matricular(self, aluno):
        self.alunos.append(aluno)

    def minutos_totais(self):
        return sum(aluno.minutos() for aluno in self.alunos)

a1 = Aluno()
a1.novo_treino("musculação", 60)
a1.novo_treino("esteira", 30)

a2 = Aluno()
a2.novo_treino("natação", 45)

academia = Academia()
academia.matricular(a1)
academia.matricular(a2)
print(academia.minutos_totais())

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# 135
