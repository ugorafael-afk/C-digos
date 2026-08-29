cor = input("Digite uma cor: verde, amarelo, vermalho: ")

cor = cor.lower()

if cor == "verde":
    print("Sinal aberto, pode Passar!")
elif cor == "amarelo":
    print("Atenção, pode passar mais não playboy!")
elif cor == "vermelha":
    print("Fecho meu patrão, pode mais não RAPA!")
else:
    print("Cor INVALIDA")