# Aula 09 · Exercício 07 (casa, opcional): o sensor de temperatura
#
# Escreva a classe Sensor do diagrama:
#   https://poo.leoad.com.br/images/aula-09/ex07-sensor.svg
# limite e total     sublinhados: atributos de classe. total conta os
#                    sensores criados.
# temperatura        @property com setter. O setter RECUSA menos de -50:
#                        raise ValueError("temperatura impossível")
#                    e só depois guarda em self._temperatura.
# de_texto           @classmethod. Recebe "Cozinha;42.5".
# alerta()           RETORNA True se a temperatura passou do limite.
# __str__            Cozinha: 42.5 graus
# __repr__           Sensor('Cozinha', 42.5)
#
# Teste você mesmo: no fim do arquivo, crie sensores (um pelo de_texto),
# mostre o alerta de cada um e provoque a recusa dentro de um try/except.
#
# SE TRAVAR, REVEJA:
#   a caixa da classe ...... aula 09, slide 8  https://poo.leoad.com.br/aulas/aula-09/#s8
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27

class Sensor:
    total = 0

    def __init__(self, temperatura, local):
        self._temperatura = temperatura
        self.local = local
        Sensor.total += 1

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -50:
            raise ValueError("temperatura impossível")
        self._temperatura = valor

    @classmethod
    def de_texto(cls, texto):
        local, temp = texto.split(";")
        return cls(float(temp), local)

    def alerta(self):
        return self._temperatura > 40

    def __str__(self):
        return f"{self.local}: {self._temperatura}"
    def __repr__(self):
        return f"Sensor ('{self.local}', {self._temperatura})"

t1 = Sensor(42.5, "Cozinha")
t2 = Sensor.de_texto("Sala;-60")
print(t1.alerta())
print(t2.alerta())
print(Sensor.total)
print(t1)
print(repr(t2))

# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-09. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# True
# False
# 2
# Cozinha: 42.5
# Sensor ('Sala', -60.0)
