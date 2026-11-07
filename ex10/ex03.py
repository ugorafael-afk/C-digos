# Aula 10 · Exercício 03 (casa, OBRIGATÓRIO): o repositório de alunos
#
# Parte 1: complete a classe Aluno. O __init__ já está pronto e passa pelo
# setter (self.media = media).
#   media       @property com setter. O setter RECUSA média fora de 0 a 10:
#                   raise ValueError("a média vai de 0 a 10")
#               e só depois guarda em self._media.
#   __str__     RETORNA, por exemplo:  Bruno (2026002): média 6.0
#
# Parte 2: crie a classe RepositorioAlunos, que guarda os alunos num
# dicionário: a chave é a matrícula, o valor é o objeto Aluno.
#   __init__()          cria self._alunos como um dicionário vazio.
#   adicionar(aluno)    guarda o aluno, usando a matrícula dele como chave.
#   buscar(matricula)   RETORNA o aluno, ou None se a matrícula não existir.
#                       Use .get().
#   remover(matricula)  se a matrícula existir, apaga o aluno e RETORNA True;
#                       se não existir, RETORNA False (sem dar erro).
#   quantidade()        RETORNA quantos alunos estão guardados.
#   melhor()            RETORNA o ALUNO (o objeto) com a maior média.
#                       Use max com key, sobre os valores do dicionário.
# Nenhum print dentro dos métodos.
#
# SE TRAVAR, REVEJA:
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25
#   dicionário ............. aula 10, slide 33  https://poo.leoad.com.br/aulas/aula-10/#s33
#   [ ] × .get() ........... aula 10, slide 34  https://poo.leoad.com.br/aulas/aula-10/#s34
#   repositório ............ aula 10, slide 40  https://poo.leoad.com.br/aulas/aula-10/#s40
#   dicionário no __init__ . aula 10, slide 42  https://poo.leoad.com.br/aulas/aula-10/#s42
#   max e min .............. aula 10, slide 26  https://poo.leoad.com.br/aulas/aula-10/#s26


class Aluno:
    def __init__(self, matricula, nome, media):
        self.matricula = matricula
        self.nome = nome
        self.media = media  

    @property
    def media(self):
        return self._media
    
    @media.setter
    def media(self, valor):
        if valor < 0 or valor > 10:
            raise ValueError("a média vai de 0 a 10")
        self._media = valor
        
    def __str__(self):
        return f"{self.nome} ({self.matricula}): média {self.media}"

    def __repr__(self):
        return f"Aluno('{self.matricula}', '{self.nome}', {self.media})"


class RepositorioAlunos:
    def __init__(self):
        self._alunos = {}
        
    def adicionar(self, aluno):
        self._alunos[aluno.matricula] = aluno
        
    def buscar(self, matricula):
        return self._alunos.get(matricula)
    
    def remover(self, matricula):
        if matricula in self._alunos:
            del self._alunos[matricula]
            return True
        return False
        
    def quantidade(self):
        return len(self._alunos)
    
    def melhor(self):
        return max(self._alunos.values(), key=lambda aluno: aluno.media)


# ===== TESTE (não altere estas linhas) =====
repo = RepositorioAlunos()
repo.adicionar(Aluno("2026001", "Ana", 8.5))
repo.adicionar(Aluno("2026002", "Bruno", 6.0))
repo.adicionar(Aluno("2026003", "Caio", 9.2))

print(repo.quantidade())          # 3
print(repo.buscar("2026002"))     # Bruno (2026002): média 6.0
print(repo.buscar("2026999"))     # None
print(repo.melhor().nome)         # Caio

print(repo.remover("2026003"))    # True
print(repo.remover("2026003"))    # False
print(repo.melhor().nome)         # Ana

recusado = 0
try:
    Aluno("2026004", "Duda", 11)
except ValueError as erro:
    print(erro)                   # a média vai de 0 a 10
    recusado = recusado + 1

ana = repo.buscar("2026001")
try:
    ana.media = -1
except ValueError:
    recusado = recusado + 1
print(ana.media)                  # 8.5

outro = RepositorioAlunos()
print(outro.quantidade())         # 0

print(f"chave: {repo.quantidade()}-{repo.buscar('2026001').nome}-{repo.melhor().media}-{repo.buscar('2026999')}-{repo.remover('2026999')}-{outro.quantidade()}-{recusado}-{len(str(repo.buscar('2026002')))}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-10. O nome tem que ser ex03.py.
# ============================================================
# SAÍDA:
