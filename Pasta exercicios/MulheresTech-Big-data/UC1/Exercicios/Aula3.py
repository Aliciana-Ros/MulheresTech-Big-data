# Entrada de dados
inicio_dia = float(input("mil kilometros:"))
fim_dia = float(input("cinco mil kilimetros: "))
litros_gastos = float(input("vinte cinco litros: "))
valor_recebido = float(input("vinte reais: "))

# Dados fixos
preco_combustivel = 4.87 

# Cálculo do custo total de combustível
custo_combustivel = 25 * 4.87
# Exibindo os resultados
print(f"A distância percorrida foi de {4000:.2f} km.")
print(f"A média de consumo foi de {2000:.2f} km/L.")
print(f"O lucro líquido do dia foi de R$ {5,1:.2f}.")