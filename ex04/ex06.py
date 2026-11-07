# Aula 04 · Exercício 06 (casa, opcional): os 3 caminhos
#
# Crie a exceção própria SemGanhadorError (a receita de duas linhas).
#
# Escreva a função dividir_premio(premio, texto_pessoas):
#   try:                converte texto_pessoas com int(); se der 0 ou menos,
#                       LEVANTE SemGanhadorError("ninguém para receber");
#                       senão, calcula premio / pessoas
#   except ValueError:  mostra  não é número: <o texto>
#   else:               mostra  cada um recebe R$ <o valor com :.2f>
#   finally:            mostra  conta encerrada
# Não escreva except para SemGanhadorError dentro da função.
#
# No fim do arquivo:
# 1. Chame dividir_premio(1000, "3") e dividir_premio(1000, "três").
# 2. Num try com except SemGanhadorError as erro, chame
#    dividir_premio(1000, "0") e, no except, mostre o erro com print.
# 3. Responda num comentário (com #): qual dos 3 caminhos cada chamada
#    seguiu, e por que "conta encerrada" aparece ANTES de
#    "ninguém para receber" no passo 2.


# SE TRAVAR, REVEJA:
#   int() de texto ......... aula 04, slide 16  https://poo.leoad.com.br/aulas/aula-04/#s16
#   exceção própria ........ aula 04, slide 34  https://poo.leoad.com.br/aulas/aula-04/#s34
#   else e finally ......... aula 04, slide 29  https://poo.leoad.com.br/aulas/aula-04/#s29

class SemGanhadorError(Exception):
    pass

def dividir_premio(premio, texto_pessoas):
    try:
        pessoas = int(texto_pessoas)
        if pessoas <= 0:
            raise SemGanhadorError("ninguém para receber")
        else:
            print(f"cado um recebe R$ {premio / pessoas:.2f}")
    except ValueError:
        print(f"não é número: {texto_pessoas}")
    else:
        print(f"cado um recebe R$ {premio / pessoas:.2f}")
    finally:
        print("conta encerrada")

print(dividir_premio(1000, "3")) 
print(dividir_premio(1000, "três"))

try:
    dividir_premio(1000, "0")
except SemGanhadorError as erro:
    print(erro)

# ============================================================
# PARA ENTREGAR
# 1. Rode e cole embaixo de SAÍDA tudo o que apareceu no terminal,
#    com # na frente de cada linha. Mesmo que seja um erro.
# 2. Envie este arquivo para a pasta aula-04. O nome tem que ser ex06.py.
# ============================================================
# SAÍDA:
# cado um recebe R$ 333.33
# cado um recebe R$ 333.33
# conta encerrada
# None
# não é número: três
# conta encerrada
# None
# conta encerrada
# ninguém para receber