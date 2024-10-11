# Entrada de dados
inicio_dia = float(input("Digite a marcação do odômetro no início do dia (em km): "))
fim_dia = float(input("Digite a marcação do odômetro no final do dia (em km): "))
litros_gastos = float(input("Digite a quantidade de litros de combustível gastos: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (em R$): "))


preco_combustivel = 4.87  

# Cálculo da distância percorrida
distancia_percorrida = fim_dia - inicio_dia


media_consumo = distancia_percorrida / litros_gastos


custo_combustivel = litros_gastos * preco_combustivel


lucro_liquido = valor_recebido - custo_combustivel

# Exibindo os resultados
print(f"A distância percorrida foi de {distancia_percorrida:.2f} km.")
print(f"A média de consumo foi de {media_consumo:.2f} km/L.")
print(f"O lucro líquido do dia foi de R$ {lucro_liquido:.2f}.")
