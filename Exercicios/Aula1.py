# Entrada de dados
potencia_lampada = float(input("Informe a potência da lâmpada(watts):"))
largura_comodo = float(input("Informe a largura do cômodo: "))
comprimento_comodo = float(input("Informe o comprimento do cômodo: "))

# Cálculo da área do cômodo
area_comodo = largura_comodo * comprimento_comodo

# Potência necessária para iluminar o cômodo 
potencia_real= area_comodo * 3


numero_bocais = area_comodo / 3


numero_lampadas = potencia_real / potencia_lampada

# Exibição do resultado
print(f"Número de bocais necessários: {numero_bocais:}")
print(f"Número de lâmpadas necessárias: {numero_lampadas:.2f}")
