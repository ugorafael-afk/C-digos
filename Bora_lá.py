nome = input("digite seu nome: ")

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
nota3 = float(input("digite sua terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Você foi aprovado! parabens! ")
elif media >= 5 and media < 7:
    print("Você este de reculperação! estude mais!")
else:
    print("Reprovado!")

print(f"O/a aluno/a {nome} sua media é {media}")