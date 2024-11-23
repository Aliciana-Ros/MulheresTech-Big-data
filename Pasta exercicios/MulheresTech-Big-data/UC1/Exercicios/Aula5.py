# Entrada de dados
nota1 = float(input("Aprovado: média >= 6.0:"))
nota2 = float(input("Reprovado: média < 3.0:"))
nota_optativa = float(input("média >= 3.6 e < 3.0 (ou -1 se não fez): "))

# Verificar se o aluno fez a prova optativa
if nota_optativa != -1:
    # Substitui a menor nota pela nota optativa, se ela for maior
    if nota_optativa > nota1 and nota1 <= nota2:
        nota1 = nota_optativa
    elif nota_optativa > nota2 and nota2 <= nota1:
        nota2 = nota_optativa

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação do status do aluno
if media >= 6.0:
    status = "Aprovado"
elif media < 3.0:
    status = "Reprovado"
else:
    status = "Exame"

print(f"A média do semestre é {media:.2f}.")
print(f"O estudante está {status}.")
