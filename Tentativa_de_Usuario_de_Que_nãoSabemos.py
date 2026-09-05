senha_correta = "eu sou o dolglas"
tentativas = 0
senha = ""

usuario = "UgoADM"
tentativas = 0
usuario = ""
while usuario != "UgoADM" and tentativas < 3 or senha != senha_correta and tentativas < 3:
    usuario = input("Digite seu nome de Usuario: ")
    senha = input("digite sua senha: ")
    tentativas += 1
if usuario == "UgoADM" and senha == senha_correta:
    print("Acesso Permitido, Ligando para todos os vingadores")
else:
    print("Acesso Negado. Passa amanhã")

while True:
    comando = input("Gostaria de Sair: ")
    if comando == "Sair":
         break 