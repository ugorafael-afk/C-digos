# Aula 04 · Exercício 08 (casa, desafio): o elevador
#
# Crie duas exceções próprias, com a receita da aula:
# AndarInvalidoError e CargaExcedidaError.
#
# Classe Elevador: o __init__ recebe ultimo_andar e carga_maxima (em kg).
# Todo elevador nasce com self.andar = 0 e self.carga = 0.
# entrar(peso)    se carga + peso passar da carga_maxima, LEVANTE
#                 CargaExcedidaError com uma mensagem que diga quantos kg
#                 passaram (ex.: passou 40 kg); senão, soma o peso à carga.
# ir_para(andar)  se o andar for menor que 0 ou maior que ultimo_andar,
#                 LEVANTE AndarInvalidoError (ex.: não existe o andar 15);
#                 senão, muda self.andar.
#
# Função viagem(elevador, pesos, andar): faz entrar cada peso da lista, com
# um for, e depois chama ir_para(andar). Ela NÃO tem try: deixa os erros
# subirem para quem chamou.
#
# No fim do arquivo, crie um Elevador(10, 600) para cada viagem e faça pelo
# menos 3 viagens. Cada uma num try com um except para cada exceção própria
# (mostrando a mensagem) e um finally que mostra o andar e a carga.
# Uma viagem tem que dar certo, outra tem que passar da carga e outra tem
# que pedir um andar que não existe. Na que passa da carga, o elevador saiu
# do andar 0? Explique num comentário (com #).


# SE TRAVAR, REVEJA:
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34
#   else e finally ......... aula 04, slide 29  https://poo.leoad.com.br/aulas/aula-04/#s29

class AndarInvalidoError(Exception):
    pass
class CargaExcedidaError(Exception):
    pass

class Elevador:
    def __init__(self, ultimo_andar, carga_maxima):
        self.ultimo_andar = ultimo_andar
        self.carga_maxima = carga_maxima
        self.andar = 0
        self.carga = 0
    
    def entrar(self, peso):
        if self.carga + peso > self.carga_maxima:
            raise CargaExcedidaError(f"passou {self.carga + peso - self.carga_maxima} kg")
        self.carga += peso

    def ir_para(self, andar):
        if andar < 0 or andar > self.ultimo_andar:
            raise AndarInvalidoError(f"não existe o andar {andar}")
        self.andar = andar

def viagem(elevador, pesos, andar):
    for peso in pesos:
        elevador.entrar(peso)
        elevador.ir_para(andar)
try:
    e1 = Elevador(10, 600)
    viagem(e1, [70, 80, 90], 5)
except CargaExcedidaError as erro:
    print(erro)
except AndarInvalidoError as erro:
    print(erro)
finally:
    print(f"Elevador no andar {e1.andar} com carga {e1.carga} kg")
try:
    e2 = Elevador(10, 600)
    viagem(e2, [200, 250, 200], 3)
except CargaExcedidaError as erro:
    print(erro)
except AndarInvalidoError as erro:
    print(erro)
finally:
    print(f"Elevador no andar {e2.andar} com carga {e2.carga} kg")
try:
    e3 = Elevador(10, 600)
    viagem(e3, [50, 60], 15)
except CargaExcedidaError as erro:
    print(erro)
except AndarInvalidoError as erro:
    print(erro)
finally:
    print(f"Elevador no andar {e3.andar} com carga {e3.carga} kg")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex08.py.
# ============================================================
# SAÍDA:
# Elevador no andar 5 com carga 240 kg
# passou 50 kg
# Elevador no andar 3 com carga 450 kg
# não existe o andar 15
# Elevador no andar 0 com carga 50 kg
