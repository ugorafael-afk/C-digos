# Aula 04 · Exercício 07 (casa, opcional): a turma cheia
#
# Crie a exceção TurmaCheiaError, com a receita da aula:
#     class TurmaCheiaError(Exception):
#         pass
#
# Classe Turma: o __init__ recebe nome e vagas, e toda turma nasce com
# self.alunos = [] (lista vazia).
# vagas              @property SÓ DE LEITURA (sem setter): o __init__ grava
#                    em self._vagas, e a property RETORNA self._vagas.
# __str__            RETORNA, por exemplo:  POO: 2 de 3 vagas ocupadas
# matricular(aluno)  se aluno for um texto vazio (""), LEVANTE
#                    ValueError("nome do aluno vazio");
#                    se a turma já tiver tantos alunos quanto vagas (use len),
#                    LEVANTE TurmaCheiaError com uma mensagem como
#                    "a turma POO já tem 3 alunos";
#                    senão, coloca o aluno na lista com append.
#
# Teste você mesmo: no fim do arquivo, crie uma Turma("POO", 3) e, com um
# for, tente matricular esta lista:
#     ["Ana", "", "Bruno", "Caio", "Duda"]
# Cada matrícula num try, com um except para ValueError e outro para
# TurmaCheiaError, mostrando a mensagem do erro, e um else que mostra
# "matriculado: <nome>". No fim, mostre a turma com print(turma), que usa o
# seu __str__, e a lista de alunos.


# SE TRAVAR, REVEJA:
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34
#   vários except .......... aula 04, slide 24  https://poo.leoad.com.br/aulas/aula-04/#s24
#   else e finally ......... aula 04, slide 29  https://poo.leoad.com.br/aulas/aula-04/#s29
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class TurmaCheiaError(Exception):
    pass

class Turma:
    def __init__(self, nome, vagas):
        self.nome = nome
        self._vagas = vagas
        self.alunos = []

    @property
    def vagas(self):
        return self._vagas

    def __str__(self):
        return f"{self.nome}: {len(self.alunos)} de {self._vagas} vagas ocupadas"
        
    def matricular(self, aluno):
        if aluno == "":
            raise ValueError("nome do aluno vazio")
        if len(self.alunos) >= self._vagas:
            raise TurmaCheiaError(f"a turma {self.nome} já tem {self._vagas} alunos")
        self.alunos.append(aluno)

print("=============================")
t1 = Turma("POO", 3)
for a in ["Ana", "", "Bruno", "Caio", "Duda"]:
    try:
        t1.matricular(a)
    except ValueError as erro:
        print(erro)
    except TurmaCheiaError as erro:
        print(erro)
    else:
        print(f"matriculado: {a}")

print(str(t1))
 
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# matriculado: Ana
# nome do aluno vazio
# matriculado: Bruno
# matriculado: Caio
# a turma POO já tem 3 alunos
# POO: 3 de 3 vagas ocupadas
