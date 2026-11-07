# Aula 05 · Exercício 05 (casa, OBRIGATÓRIO): a classe Contato
#
# Atributo de CLASSE: total = 0 (quantos contatos já foram criados).
# O __init__ recebe nome, telefone e cidade, guarda os três e soma 1 em
#   Contato.total (pela classe, não pelo self), DEPOIS de guardar o telefone.
#   telefone    @property e @telefone.setter. O setter RECUSA telefone que
#               não tenha 11 caracteres (use len):
#                   raise ValueError("telefone precisa de 11 dígitos")
#   cidade é opcional e vale "Goiânia" quando ninguém mandar.
# de_texto(texto)  construtor alternativo, com @classmethod. Recebe um texto
#                  como "Bia;62988887777;Anápolis", corta no ; com split e
#                  RETORNA cls(nome, telefone, cidade).
# __repr__         retorna, por exemplo: Contato('Bia', '62988887777', 'Anápolis')
#
# Exemplos:
#   Contato("Ana", "62999990000") tem cidade Goiânia.
#   Com a lista de textos abaixo, um for que chama Contato.de_texto em cada
#   linha e guarda o resultado numa lista nova mostra, no print da lista:
#   [Contato('Bia', '62988887777', 'Anápolis'), Contato('Caio', '62977776666', 'Trindade'), Contato('Duda', '64966665555', 'Rio Verde')]
#   Depois de criar a Ana e os 3 da lista, Contato.total vale 4.
#   Contato("Eva", "6299") é recusado com ValueError, e o total continua 4.
#
# Use esta lista no seu teste:
#   linhas = ["Bia;62988887777;Anápolis", "Caio;62977776666;Trindade", "Duda;64966665555;Rio Verde"]
#
# Teste você mesmo: no fim do arquivo, crie os objetos e mostre os resultados
# com print. Use os exemplos acima para conferir.
#
# SE TRAVAR, REVEJA:
#   contador ............... aula 05, slide 21  https://poo.leoad.com.br/aulas/aula-05/#s21
#   valor padrão ........... aula 05, slide 6  https://poo.leoad.com.br/aulas/aula-05/#s6
#   construtor alternativo . aula 05, slide 27  https://poo.leoad.com.br/aulas/aula-05/#s27
#   setter que recusa ...... aula 04, slide 19  https://poo.leoad.com.br/aulas/aula-04/#s19
#   __repr__ ............... aula 02, slide 27  https://poo.leoad.com.br/aulas/aula-02/#s27

class Contato:
    total = 0

    def __init__(self, nome, telefone, cidade = "Goiania"):
        self.nome = nome
        self._telefone = telefone
        self.cidade = cidade
        Contato.total += 1

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if len(valor) != 11:
            raise ValueError("telefone precisa de 11 dígitos")

    @classmethod
    def de_texto(cls, texto):
        partes = texto.split(";")
        return cls(partes[0], partes[1], partes[2])

    def __repr__(self):
        return f"Contato '{self.nome}', '{self.telefone}', '{self.cidade}'"

c1 = Contato("Ugo", "23045876761")
print(c1)

linhas = ["Bia;62988887777;Anápolis", "Caio;62977776666;Trindade", "Duda;64966665555;Rio Verde"]

for linha in linhas:
    c = Contato.de_texto(linha)
    print(c)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-05. O nome tem que ser ex05.py.
# ============================================================
# SAÍDA:
# Contato 'Ugo', '23045876761', 'Goiania'
# Contato 'Bia', '62988887777', 'Anápolis'
# Contato 'Caio', '62977776666', 'Trindade'
# Contato 'Duda', '64966665555', 'Rio Verde'