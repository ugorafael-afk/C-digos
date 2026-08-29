nome = input("Informe seu nome: ")
peso = int(input("Informe seu peso, por gentileza: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc > 25:
    massa_muscular = int(input("Digite sua massa muscular: "))
    if massa_muscular > 5:
        print("===TÁ BÃO===")
    else:
        print("===TÁ GORDINHOOOO===")
elif imc > 18 and imc <= 25:
    print("===TÁ SHOW DE BOLA===")
else:
    print("tá precisando comer, viu bixinhooo!!")

print(f"Seu nome é {nome}, imc é {imc:.2f}")