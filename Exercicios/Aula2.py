# Entrada de dados
comprimento = float(input("Informe o comprimento da cozinha (em metros): "))
largura = float(input("Informe a largura da cozinha (em metros): "))
altura = float(input("Informe a altura da cozinha (em metros): "))

# Cálculo da área das paredes

area_paredes = 2 * (largura * altura) + 2 * (comprimento * altura)

# Cada caixa de azulejos cobre 1,5 m²
area_por_caixa = 1.5


quantidade_caixas = area_paredes / area_por_caixa

# Exibição do resultado
print(f"Quantidade de caixas de azulejos necessárias: {quantidade_caixas:.0f}")
