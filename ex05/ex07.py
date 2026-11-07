# Aula 05 · Exercício 07 (casa, opcional): Playlist e Musica (associação)
#
# Musica: o __init__ recebe titulo e segundos.
#   segundos  @property e @segundos.setter. O setter RECUSA 0 ou menos:
#                 raise ValueError("música precisa durar")
#   __repr__  retorna, por exemplo: Musica('Evidências', 300)
# Playlist: o __init__ recebe nome, guarda, e cria self.musicas como lista vazia.
#   adicionar(musica)  recebe uma Musica JÁ CRIADA fora da playlist (associação)
#                      e coloca na lista.
#   duracao_total()    RETORNA a soma dos segundos de todas as músicas, usando um for.
#   minutos()          RETORNA a duração total dividida por 60.
#
# Exemplos:
#   evidencias = Musica("Evidências", 300) e tempo = Musica("Tempo Perdido", 240).
#   Uma playlist com as duas: duracao_total() retorna 540 e minutos() retorna 9.0.
#
# No fim, coloque a MESMA música em duas playlists e mostre, com print, que
# é um objeto só: compare com == a música das duas listas (dá True).
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   associação ............. aula 05, slide 39  https://poo.leoad.com.br/aulas/aula-05/#s39
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

class Musica:
    def __init__(self, titulo, segundos):
        self.titulo = titulo
        self.segundos = segundos

    @property
    def segundos(self):
        return self._segundos
    
    @segundos.setter
    def segundos(self, valor):
        if valor <= 0:
            raise ValueError("música precisa durar")
        self._segundos = valor

    def __repr__(self):
        return f"Música('{self.titulo}', {self.segundos})"

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar(self,musica):
        self.musicas.append(musica)

    def duracao_total(self):
        total = 0
        for musica in self.musicas:
            total += musica.segundos
        return total

    def minutos(self):
        return self.duracao_total() / 60

print("=======================")
m1 = Musica("Evidências", 300)
m2 = Musica("Tempo Perdido", 240)
p1 = Playlist("Rock")
p1.adicionar(m1)
p1.adicionar(m2)
print(p1.duracao_total())
print(p1.minutos())
p2 = Playlist("MPB")
p2.adicionar(m1)
print(p1.musicas[0] == p2.musicas[0])

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
