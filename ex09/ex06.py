# Aula 09 · Exercício 06 (casa, opcional): o streaming
#
# Escreva as 3 classes do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex06-streaming.svg
# A Serie CRIA os próprios episódios (losango cheio). O Usuario RECEBE
# séries prontas (linha simples): várias pessoas assistem à mesma série.
#
# Serie.novo_episodio(titulo, minutos)  cria o Episodio e guarda na lista.
# Serie.duracao()                       RETORNA a soma dos minutos.
# Usuario.assistir(serie)               guarda a série recebida.
# Usuario.minutos_assistidos()          RETORNA a soma da duracao() das séries.
#
# Mostre também que duas pessoas assistindo à MESMA série guardam o mesmo
# objeto: compare com == as séries das duas listas.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print.
#
# SE TRAVAR, REVEJA:
#   linhas do diagrama ..... aula 09, slide 15  https://poo.leoad.com.br/aulas/aula-09/#s15
#   composição ............. aula 05, slide 42  https://poo.leoad.com.br/aulas/aula-05/#s42

class Episodio:
    def __init__(self, titulo, minutos):
        self.titulo = titulo
        self.minutos = minutos

class Serie:
    def __init__(self):
        self.episodios = []

    def novo_episodio(self, titulo, minutos):
        episode = Episodio(titulo, minutos)
        self.episodios.append(episode)

    def duracao(self):
        return sum(episode.minutos for episode in self.episodios)

class Usuario:
    def __init__(self):
        self.series = []

    def assistir(self, serie):
        self.series.append(serie)

    def minutos_assistidos(self):
        return sum(serie.duracao() for serie in self.series)

s1 = Serie()
s1.novo_episodio("Episódio 1", 45)  
s2 = Serie()
s2.novo_episodio("Episódio 1", 30)

u1 = Usuario()
u1.assistir(s1)

u2 = Usuario()
u2.assistir(s2)

print(u1.minutos_assistidos())
print(u2.minutos_assistidos())

    
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# 45
# 30