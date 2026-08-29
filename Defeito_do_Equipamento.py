horas = int(input("Digite a quantidade de carga horaria do equipamento: "))
defeito = input("Seu equipamento possui algum defeito? (sim/não): ")

if defeito.lower() == "sim":
    print("Leva essa BOMBA pro tecnico agora, meu patrão!")
elif defeito.lower() == "não" and horas >= 500:
    print("Tá certinho Majo, só não esquece de levar pro tecnico depois, beleza?")
else:
    print("Tá certinho. Novim pai!!")