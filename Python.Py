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


# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def main():
    N = int(input("Quantas pessoas você quer calcular o IMC? "))
    for i in range(N):
        print(f"\nPessoa {i+1}:")
        altura = float(input("Digite a altura em metros: "))
        peso = float(input("Digite o peso em kg: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"O IMC é {imc:.2f} e a classificação é: {classificacao}")

if __name__ == "__main__":
    main()



#Em seguida, todas as funções devem ser integradas em um único programa: criem uma nova função para gerar números aleatórios e aplicá-los 
# às operações anteriores.

import random

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def gerar_peso_altura():
    altura = round(random.uniform(1.5, 2.0), 2)  
    peso = round(random.uniform(50.0, 120.0), 1)  
    return peso, altura

def main():
    N = int(input("Quantas pessoas você quer calcular o IMC? "))
    
    for i in range(N):
        print(f"\nPessoa {i+1}:")
        peso, altura = gerar_peso_altura()
        print(f"Altura gerada: {altura} m")
        print(f"Peso gerado: {peso} kg")
        
