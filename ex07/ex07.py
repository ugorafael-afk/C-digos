# Aula 07 · Exercício 07 (casa, opcional): avisos com duck typing
#
# Crie três classes SEM herança, todas com o método enviar(msg), que RETORNA um texto:
#   Email(endereco)   enviar("Intervalo às 20h10")  retorna  E-mail para ana@email.com: Intervalo às 20h10
#   Sms(numero)       enviar("Intervalo às 20h10")  retorna  SMS para 62 99999-0000: Intervalo às 20h10
#                     numero com @property e @numero.setter. O setter RECUSA
#                     número com menos de 8 caracteres (use len):
#                         raise ValueError("número inválido")
#                     O __init__ faz self.numero = numero: o setter roda na criação.
#   Telao           enviar("Intervalo às 20h10")  retorna  TELÃO: Intervalo às 20h10
# Crie a função avisar_todos(canais, msg), que RETORNA uma lista com o texto de
# cada canal, na ordem (comece com textos = [] e use append). Sem nenhum if.
#
# Depois crie a classe Pombo com o método mandar(msg) e coloque um Pombo() na
# lista de canais. Rode, leia o erro e escreva num comentário o que ele quer dizer.
# Por fim, conserte a classe Pombo (sem mexer na função) para ela entrar no aviso:
#   Pombo()   enviar("Intervalo às 20h10")  retorna  Pombo levou: Intervalo às 20h10
# Na SAÍDA, cole a saída final, já com o Pombo consertado.
#
# Teste você mesmo: no fim do arquivo, crie os canais e mostre os resultados
# com print. Use os exemplos acima para conferir. Mostre também, com
# try/except, que Sms("190") é recusado.
#
# SE TRAVAR, REVEJA:
#   duck typing ............ aula 07, slide 13  https://poo.leoad.com.br/aulas/aula-07/#s13
#   assinatura ............. aula 07, slide 19  https://poo.leoad.com.br/aulas/aula-07/#s19
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   try/except ............. aula 04, slide 13  https://poo.leoad.com.br/aulas/aula-04/#s13

class Email:
    def __init__(self, endereco):
        self.endereco = endereco

    def enviar(self, msg):
        return f"Email para {self.endereco}: {msg}"

class Sms:
    def __init__(self, numero):
        self.numero = numero

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if valor is None or len(valor) < 8:
            raise ValueError("número inválido")
        self._numero = valor

    def enviar(self, msg):
        return f" Sms para {self.numero}: {msg}"

class Telão:
    def enviar(self, msg):
        return f" TELÃO: {msg}"

    def avisar_todos(canais, msg):
        textos = []
        for canal in canais:
            textos.append(canal.enviar(msg))
        return textos

class Pombo:
    def enviar(self, msg):
        return f"Pombo levou: {msg}"


e1 = Email("ana@gmail.com")
s1 = Sms("62 99999-0000")
t1 = Telão()
p1 = Pombo()

canais = [e1, s1, t1, p1]
for canal in canais:
    print(canal.enviar("Intervalo às 20h10"))

try:
    s2 = Sms("190")
except ValueError:
    print("Número inválido")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-07. O nome tem que ser ex07.py.
# ============================================================
# SAÍDA:
# Email para ana@gmail.com: Intervalo às 20h10
# Sms para 62 99999-0000: Intervalo às 20h10
# TELÃO: Intervalo às 20h10
# Pombo levou: Intervalo às 20h10
# Número inválido