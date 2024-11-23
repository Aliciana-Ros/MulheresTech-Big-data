### ESTRUTURAS DE REPETIÇÃO ###

#FOR: sabemos a quantidade de vezes que o laço de repetição 

# for i in range(5):
#  numero=int(input('Digite um número:'))
#  print(f'Dobro:{numero*2}')

#WHILE: queremos a repetição quando a condição for  verdadeiro

#Exemplo1:
# contador=0
# while True:
# numero=int(input('Digite um número:'))
# print(f'Triplo:{numero*3}')
# contador=contador+1

#Exemplo2:
# DO WHILE: similar ao 'WHILE', mas garante que o bloco seja lido ao menos 1 vez
# antes da verificação da condição.

# num=5
# while True:
#   print('teste')
#   if not(num<3):
#    break
  
#   #Exemplo3:
# num=5
# while num<3:
#     print('teste')


#>>>Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
#menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
#experiência profissional.

#RESOLUÇÃO:

# Variável para armazenar os candidatos válidos
candidatos = []
contador = 0  
# Contador para garantir que 10 candidatos sejam processados

# Enquanto não atingirmos 10 candidatos válidos
while contador < 3:
    nome = input("Digite o nome do candidato: ")
    idade = int(input("Digite a idade do candidato: "))
    
    # Verificar se o candidato tem idade mínima de 18 anos
    if idade < 18:
        print("Candidato menor de idade. Não pode participar.")
    else:
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        formacao = input("Digite a formação acadêmica: ")
        experiencia = input("Digite a experiência profissional: ")
        
        # Armazenar os dados do candidato
        candidatos.append({
            'nome': nome,
            'idade': idade,
            'telefone': telefone,
            'email': email,
            'formacao': formacao,
            'experiencia': experiencia
        })
        
        contador += 1  # Incrementa o contador para processar o próximo candidato

# Exibe a quantidade de candidatos válidos cadastrados
print(f"{len(candidatos)} candidatos cadastrados com sucesso.")