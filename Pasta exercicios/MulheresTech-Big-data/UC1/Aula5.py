# Entrada de dados
nota1 = float(input("primeira nota:"))
nota2 = float(input(" Segunda nota: "))
nota_optativa = float(input("Informe a nota da avaliação optativa (ou -1 se não fez):"))

# Verificar se o aluno fez a prova optativa
if nota_optativa != -1:
    # Substitui a menor nota pela nota optativa, se ela for maior
     menor_nota=min(nota1,nota2)
if nota_optativa>menor_nota:
   if nota1 == menor_nota:
       nota1 = nota_optativa
   else:
     nota2 = nota_optativa

# Cálculo da média
media = (nota1 + nota2)/2
print(f'Média:{media}')

# Verificação do resultado do aluno
if media >= 6.0:
    print = ("Aprovado")
elif media < 3.0:
    print = ("Reprovado")
else:
    print = ("Exame de Recuperação")

# Exibindo os resultados
print(f"A média do semestre é {media:.2f}.")
print(f"O estudante está {status}.")
