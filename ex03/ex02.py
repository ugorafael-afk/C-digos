# Aula 03 · Exercício 02 (sala): a bateria do Celular
#
# Crie a classe Celular.
# O __init__ recebe marca e bateria. A marca fica pública (self.marca).
# A bateria entra PELO SETTER: self.bateria = bateria.
# bateria   @property: RETORNA o valor guardado em self._bateria.
#           @bateria.setter: CORRIGE o valor antes de guardar no self._bateria.
#           Acima de 100 vira 100; abaixo de 0 vira 0; senão, guarda como veio.
# carregar(quantidade)   soma a quantidade na bateria.
# usar(minutos)          tira 1 ponto de bateria por minuto.
# Os dois métodos mudam a bateria com self.bateria = ..., para passar pelo setter.


class Celular:
    def __init__(self, marca, bateria):
       self.marca = marca
       self.bateria = bateria

    @property
    def bateria(self):
        return self._bateria

    @bateria.setter
    def bateria(self, valor):   
        if valor > 100:
            valor = 100
        elif valor < 0:
            valor = 0
        self._bateria = valor

    def carregar(self, quantidade):
        self.bateria = self.bateria + quantidade

    def usar(self, minutos):
        self.bateria = self.bateria - minutos
# ===== TESTE (não altere estas linhas) =====
c1 = Celular("Samsung", 80)
c2 = Celular("Motorola", 130)    # nasce acima de 100

print(c1.marca, c1.bateria)      # Samsung 80
print(c2.marca, c2.bateria)      # Motorola 100

c1.carregar(50)
print(c1.bateria)                # 100
c1.usar(30)
print(c1.bateria)                # 70
c2.usar(150)
print(c2.bateria)                # 0

c3 = Celular("Apple", -10)       # nasce abaixo de 0
c3.carregar(45)
print(c3.bateria)                # 45

c4 = Celular("Nokia", 20)
c4.bateria = 250                 # gravação de fora: também passa pelo setter
print(c4.bateria)                # 100

# Só o teste olha por dentro, para conferir que o setter corrige ANTES de guardar:
print(c2._bateria, c4._bateria)  # 0 100

print(f"chave: {c1.marca}-{c2.marca}-{c1.bateria}-{c2._bateria}-{c3.bateria}-{c4.bateria}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex02.py.
# ============================================================
# SAÍDA:
