# Aula 03 · Exercício 06 (casa, opcional): a senha do Usuario
#
# Classe Usuario. O __init__ recebe login e senha (a senha pelo setter).
# login     @property só de leitura.
# senha     @property que RETORNA sempre "********": a senha de verdade,
#           guardada em self._senha, nunca sai do objeto.
#           @senha.setter: RECUSA senha com menos de 8 caracteres (use len) com
#           raise ValueError("A senha precisa ter 8 caracteres ou mais")
# verificar(tentativa)   RETORNA True se a tentativa for igual à senha
#                        guardada, senão False.
# __repr__  retorna, por exemplo: Usuario('ana.silva')
#
# Teste você mesmo: no fim do arquivo, crie pelo menos dois objetos e mostre
# os resultados com print. Troque a senha de um deles e verifique de novo.
# Se quiser ver a recusa, deixe essa tentativa como ÚLTIMA linha: o programa
# para no seu ValueError e o que vem depois não roda.

class Usuario:
    def __init__(self, login, senha):
        self._login = login
        self._senha = senha

    @property
    def login(self):
        return self._login

    @property
    def senha(self):
        return "********"

    @senha.setter
    def senha(self, valor):
        if len(valor) < 8:
            raise ValueError("A senha precisa ter 8 caracteres ou mais")
        self._senha = valor

    def verificar(self, tentativa):
        return tentativa == self._senha

    def __repr__(self):
        return f"Usuario('{self.login}')"

u1 = Usuario("ana.silva", "12345678")   
u2 = Usuario("joao.santos", "senha123")

print(u1.login, u1.senha)
print(u2.login, u2.senha)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-03. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
