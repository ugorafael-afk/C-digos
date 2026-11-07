# Aula 07 · Exercício 06 (casa, opcional): a Playlist com operadores
#
# O __init__ recebe nome e cria self.musicas = [] (lista vazia).
# nome               @property SÓ DE LEITURA (guarde em self._nome).
# adicionar(musica)  coloca a música no fim da lista. Música sem nome é recusada:
#                    se musica for "", raise ValueError("música sem nome").
# __len__            len(p) RETORNA quantas músicas a playlist tem.
# __add__            p1 + p2 RETORNA uma Playlist NOVA, com o nome "Rock + MPB"
#                    (os dois nomes ligados por " + ") e as músicas das duas, na ordem.
#                    As playlists originais não mudam.
# __lt__             p1 < p2 é True quando p1 tem MENOS músicas que p2.
# __repr__           retorna, por exemplo:  Playlist('Rock')
# Nos operadores, se o outro não for Playlist, retorne NotImplemented.
#
# Exemplo: rock com "Tempo Perdido" e "Pais e Filhos", mpb com "Aquarela".
#   print(rock + mpb)          Playlist('Rock + MPB')
#   print(len(rock + mpb))     3
#   print(mpb < rock)          True
#   print(len(rock))           2   (o + não mudou a rock)
#
# Teste você mesmo: no fim do arquivo, crie as playlists e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que rock.adicionar("") é recusado e que len(rock) continua 2.
#
# SE TRAVAR, REVEJA:
#   __lt__ e __len__ ....... aula 07, slide 36  https://poo.leoad.com.br/aulas/aula-07/#s36
#   __add__ ................ aula 07, slide 25  https://poo.leoad.com.br/aulas/aula-07/#s25
#   NotImplemented ......... aula 07, slide 30  https://poo.leoad.com.br/aulas/aula-07/#s30
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

class Playlist:
    def __init__(self, nome):
        self._nome = nome
        self.musicas = []

    @property
    def nome(self):
        return self._nome

    def adicionar(self, musica):
        if musica == "":
            raise ValueError("musica sem nome")
        self.musicas.append(musica)

    def __len__(self):
        return len(self.musicas)

    def __add__(self, outro):
        if isinstance(outro, Playlist):
            nova_playlist = Playlist(f"{self.nome} + {outro.nome}")
            nova_playlist.musicas = self.musicas + outro.musicas
            return nova_playlist
        return NotImplemented

    def __lt__(self, outro):
        if isinstance(outro, Playlist):
            return len(self) < len(outro)
        return NotImplemented

    def __repr__(self):
        return f"Playlist('{self.nome}')"

mpb = Playlist("MPB")
mpb.adicionar("Aquarela")
rock = Playlist("Rock")
rock.adicionar("Tempo Perdido")
rock.adicionar("Pais e Filhos")

print(rock + mpb)          
print(len(rock + mpb))     
print(mpb < rock)          
print(len(rock))          

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# Playlist('Rock + MPB')
# 3
# True
# 2