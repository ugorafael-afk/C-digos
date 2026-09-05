LIMITE = 3
alunos = []
print("-" * 50)
print("Boletim do aluno")
print("-" * 50)

while len(alunos) < LIMITE:
    print(f"Aluno {len(alunos) + 1} de {LIMITE}")

    nome = input("Nome do aluno: ")
    email = input("Email do aluno: ")
    matricula = input("Matrícula do aluno: ")
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    nota3 = float(input("nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5 and media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    registro= {"nome": nome, "matricula": matricula}
    registro["media"] = media
    registro["situacao"] = situacao
    registro["email"] = email
    alunos.append(registro)

print(f"Total de alunos: {len(alunos)}")

print(f"{'MATRICULA':<12} {'NOME':<25}"
        f"{'MEDIA':>8} {'SITUACAO':>15}") 
for registro in alunos:
    print(f"{registro['matricula']:<12} {registro['nome']:<25}"
     f"{registro['media']:>8.2f} {registro['situacao']:>15}")

aprovados = 0; recuperacao = 0; reprovados = 0
for registro in alunos:
    if registro["situacao"] == "Aprovado":
        aprovados += 1
    elif registro["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")