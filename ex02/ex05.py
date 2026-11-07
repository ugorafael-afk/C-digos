# Aula 02 · Exercício 07 (casa, opcional): a classe ContaBancaria
#
# O __init__ recebe titular e saldo, com saldo=0 como valor padrão.
# depositar(valor)  soma o valor no saldo.
# sacar(valor)      se tiver saldo suficiente, tira o valor e RETORNA True;
#                   senão, não mexe no saldo e RETORNA False.
# __str__           retorna, por exemplo: Conta de Ana | saldo R$ 150.00
# __repr__          retorna, por exemplo: ContaBancaria('Ana', 150)
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Use os exemplos acima para conferir.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def __str__(self):
        return f"Conta de {self.titular} | saldo R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"ContaBancaria('{self.titular}', {self.saldo})"

conta1 = ContaBancaria('Ana', 150)
conta2 = ContaBancaria('Bruno')

print(conta1)
print(conta2)
conta1.depositar(50)
print(conta1)
print(repr(conta1))
print(repr(conta2))

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-02. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA: Conta de Ana | saldo R$ 150.00
#        Conta de Bruno | saldo R$ 0.00
#        Conta de Ana | saldo R$ 200.00
#        ContaBancaria('Ana', 200)
#        ContaBancaria('Bruno', 0)