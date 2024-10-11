# Entrada de dados
nota1 = float(input(" primeira Nota "))
nota2 = float(input("Segunda Nota: "))
nota_optativa = float(input("Nota optativa: "))

# Verificar se o aluno fez a prova optativa
if nota_optativa != -1:
   menor_nota=(nota1,nota2)
   if nota_optativa > menor_nota:
      if  nota1==menor_nota:
          nota1 = nota_optativa
      else: 
        nota2 = nota_optativa


media = (nota1 + nota2) / 2

# Verificação do estado do aluno
if media >= 6.0:
    status = ("Aprovado")
elif media < 3.0:
    print = ("Reprovado")
else:
    status = ("Exame de Recuperação")

# Exibindo os resultados
print(f"A média do semestre é {media:.2f}.")
print(f"O estudante está {status}.")
