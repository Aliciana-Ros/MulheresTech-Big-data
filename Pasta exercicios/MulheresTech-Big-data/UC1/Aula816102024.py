
# FUNÇÕES:

# def somar(parametro1,parametro2): #nesse exemplo: como eu disse quem são meus argumentos, eu preciso...
#     return parametro1+parametro2
# print(somar(20,30)) #...ter a informação deles pro meu print.

# def subtrair(): #nesse exemplo, eu não disse quem são os argumentos da função, pois já tenho inputs dentro dela. Com isso...
#     parametro1=int(input('Número 1:'))
#     parametro2=int(input('Número 2:'))
#     return parametro1-parametro2

# print(subtrair()) #...eu consigo executar a função sem precisar fornecer alguma informação no print.

#EXEMPLO DE APRIMORAMENTO: (aula dia 08-out)

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

# def boletim():
#     nota1=float(input('Primeira Nota:'))
#     nota2=float(input('Segunda Nota:'))
#     nota_opt=float(input('Nota Optativa:'))

#     if nota_opt != -1: 
#         menor_nota=min(nota1,nota2)
#         if nota_opt>menor_nota:
#             if nota1==menor_nota:
#                 nota1=nota_opt
#             else:
#                 nota2=nota_opt

#     media=(nota1+nota2)/2
#     print(f'Média:{media}')

#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:  

#         print("Reprovado")
#     else:
#         print("Exame de Recuperação")

# boletim()

#Crie uma função para multiplicar dois números 


#ATIVIDADE ASSISTIDA:

#Crie uma função para multiplicar dois números quaisquer:

# def multiplicar(num1=1,num2=2):
#     num1=float(input('Digite o primeiro número:'))
#     num2=float(input('Digite o segundo número:'))
#     return f'O resultado dos dois números multiplicados é {num1*num2}.'

# print(multiplicar())

#ATIVIDADES:

#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

#Função para calcular a multa
def calcular_multa(peso_peixes, limite=100, taxa=3.00):
    # Verifica se o peso excede o limite
    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * taxa
        return multa
    else:
       
        return 0.0


peso_peixes = float(input("Digite o peso total dos peixes por quilos: "))


multa = calcular_multa(peso_peixes)

if multa > 0:
    print(f"Você excedeu o limite de 100 quilos. A multa será de R$ {multa:.2f}.")
else:
    print("Você está dentro do limite de 100 quilos. Não há multa.")

