# Aula 03 · Exercício 07 (casa, opcional): a conta que guarda os movimentos
#
# Escreva a ContaBancaria guardando, por dentro, a lista self._movimentos
# (como no slide "Mudou o jeito de guardar"). O __init__ recebe só o titular.
# titular    @property só de leitura.
# saldo      @property calculada: RETORNA a soma dos movimentos (use for).
# depositar(valor)   valor menor ou igual a zero: raise ValueError com uma
#                    mensagem sua. Senão, coloca o valor na lista.
# sacar(valor)       valor menor ou igual a zero: raise ValueError. Valor maior
#                    que o saldo: RETORNA False e não mexe. Senão, coloca
#                    -valor na lista e RETORNA True.
# extrato()          RETORNA uma CÓPIA da lista de movimentos (como no slide:
#                    com a cópia, quem usa não consegue dar append na lista
#                    de dentro e mudar o saldo), por exemplo: [100, -30]
# __str__            retorna, por exemplo: Conta de Ana | saldo R$ 70.00
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Se quiser ver a recusa, deixe essa tentativa como
# ÚLTIMA linha: o programa para no seu ValueError e o que vem depois não roda.


class ContaBancaria:
    def __init__(self, titular):
        self._titular = titular
        self._movimentos = []

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        total = 0
        for movimento in self._movimentos:
            total += movimento
        return total

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._movimentos.append(valor)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor de saque deve ser maior que zero.")
        if valor > self.saldo:
            return False
        self._movimentos.append(-valor)
        return True

    def extrato(self):
        return self._movimentos.copy()

    def __str__(self):
        return F"Conta de {self.titular} | saldo R$ {self.saldo:.2f}"

c1 = ContaBancaria("Ana")
c2 = ContaBancaria("João")

print(c1)
c1.depositar(100)
print(c1)
c1.sacar(30)
print(c1)
print(c2)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
