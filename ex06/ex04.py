# Aula 06 · Exercício 04 (casa, OBRIGATÓRIO): Conta e ContaPoupanca
#
# Conta: o __init__ recebe titular e saldo, com saldo=0 como valor padrão.
#   saldo             @property SÓ DE LEITURA (guarde em self._saldo): ninguém
#                     muda o saldo de fora, só pelos métodos.
#   depositar(valor)  soma o valor ao saldo. RECUSA valor zero ou negativo:
#                         raise ValueError("depósito inválido")
#   __str__           retorna, por exemplo:  Ana: R$ 100.00
#
# ContaPoupanca é uma Conta que rende:
#   o __init__ recebe titular, saldo e rendimento (0.01 quer dizer 1%).
#     Use super().__init__ para titular e saldo, e guarde o rendimento.
#   render()  aumenta o saldo: saldo + saldo * rendimento.
#   Exemplo: ContaPoupanca("Bia", 1000, 0.01), depois render():  Bia: R$ 1010.00
#   A poupança também deposita (herdou o depositar() do pai): não escreva de novo.
#
# Teste você mesmo: no fim do arquivo, crie uma Conta e uma ContaPoupanca,
# chame os métodos e mostre os resultados com print. Use os exemplos acima para conferir.
# Mostre também, com try/except, que depositar(-50) é recusado.
#
# SE TRAVAR, REVEJA:
#   super() ................ aula 06, slide 15  https://poo.leoad.com.br/aulas/aula-06/#s15
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   property só de leitura . aula 03, slide 15  https://poo.leoad.com.br/aulas/aula-03/#s15
#   raise .................. aula 04, slide 10  https://poo.leoad.com.br/aulas/aula-04/#s10
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13
#   __str__ ................ aula 02, slide 25  https://poo.leoad.com.br/aulas/aula-02/#s25

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("depósito inválido")
        self._saldo += valor

    def __str__(self):
        return f"{self.titular}: R$ {self.saldo:.2f}"

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, rendimento = 0.01):
        super().__init__(titular, saldo)
        self.rendimento = rendimento

    def render(self):
        self._saldo += self._saldo * self.rendimento
        return self._saldo

c1 = Conta("Ugo", 100)
c1.depositar(50)
print(c1)
c2 = ContaPoupanca("Bia", 1000, 0.01)
c2.render()
print(c2)
# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-06. O nome tem que ser ex04.py.
# ============================================================
# SAÍDA:
# Ugo: R$ 150.00
# Bia: R$ 1010.00
