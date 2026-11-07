# Aula 08 · Exercício 05 (casa, OBRIGATÓRIO): notificações
#
# Crie a classe abstrata Notificacao (herda de ABC):
#   enviadas            atributo de classe, começa em 0: conta quantas
#                       mensagens já foram enviadas, por qualquer canal.
#   __init__(destino)   guarda o destino (um e-mail ou um telefone).
#   canal               property ABSTRATA: o nome do canal.
#   formatar(mensagem)  método ABSTRATO: RETORNA a mensagem no jeito do canal.
#   enviar(mensagem)    método concreto: RETORNA, por exemplo:
#                       [E-mail] para ana@email.com: Olá! A aula começa às 18h35.
#                       (use self.canal, sem parênteses, e self.formatar(mensagem))
#                       A cada envio, some 1 em Notificacao.enviadas (pela classe).
#
# E as duas filhas:
# Email   canal "E-mail". formatar coloca "Olá! " antes da mensagem.
# SMS     canal "SMS". formatar coloca " Responda SAIR para cancelar."
#         depois da mensagem.
#
# Exemplos:
#   Email("ana@email.com").enviar("A aula começa às 18h35.")
#       [E-mail] para ana@email.com: Olá! A aula começa às 18h35.
#   SMS("62 99999-0000").enviar("Seu pedido chegou.")
#       [SMS] para 62 99999-0000: Seu pedido chegou. Responda SAIR para cancelar.
#
# No teste, coloque uma notificação de cada tipo numa lista e, com um for,
# envie a mesma mensagem por todas (imprima o que o enviar() retorna).
# Depois do for, imprima Notificacao.enviadas: ele conta todos os envios
# feitos até ali no programa, os do for e os que você fez antes.
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os
# resultados com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   classe abstrata ........ aula 08, slide 8  https://poo.leoad.com.br/aulas/aula-08/#s8
#   property abstrata ...... aula 08, slide 21  https://poo.leoad.com.br/aulas/aula-08/#s21
#   abstrato e concreto .... aula 08, slide 13  https://poo.leoad.com.br/aulas/aula-08/#s13
#   atributo de classe ..... aula 05, slide 18  https://poo.leoad.com.br/aulas/aula-05/#s18
#   contador ............... aula 05, slide 21  https://poo.leoad.com.br/aulas/aula-05/#s21

from abc import ABC, abstractmethod

class Notificacao(ABC):
    enviadas = 0

    def __init__(self, destino):
        self.destino = destino

    @property
    @abstractmethod
    def canal(self):
        pass

    @abstractmethod
    def formatar(self, mensagem):
        pass

    def enviar(self, mensagem):
        Notificacao.enviadas += 1
        return f"[{self.canal}] para {self.destino}: {self.formatar(mensagem)}"

class Email(Notificacao):
    @property
    def canal(self):
        return "E-mail"

    def formatar(self, mensagem):
        return f"Olá! {mensagem}"

class SMS(Notificacao):
    @property
    def canal(self):
        return "SMS"

    def formatar(self, mensagem):
        return f"{mensagem} Responda SAIR para cancelar."
    

lista = [ Email("ana@email.com"), SMS("62 99999-0000")]
for l in lista:
    print(l.enviar("A aula começa às 18h35."))

n1 = Email("ana@email.com")
print(n1.enviar("Hoje tem reunião às 14h."))
n2 = SMS("62 99999-0000")
print(n2.enviar("Seu pedido chegou."))
print(f"Total de notificações enviadas: {Notificacao.enviadas}")

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-08. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# [E-mail] para ana@email.com: Olá! A aula começa às 18h35.
# [SMS] para 62 99999-0000: A aula começa às 18h35. Responda SAIR para cancelar.
# [E-mail] para ana@email.com: Olá! Hoje tem reunião às 14h.
# [SMS] para 62 99999-0000: Seu pedido chegou. Responda SAIR para cancelar.
# Total de notificações enviadas: 4