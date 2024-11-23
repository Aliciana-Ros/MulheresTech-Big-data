# Entrada de dados
comprimento = float(input(" 5 metros: "))
largura = float(input("4 metros: "))
altura = float(input(" 3 metros: "))

# Cálculo da área das paredes
# A cozinha tem 4 paredes:
# 2 paredes com dimensão comprimento x altura
# 2 paredes com dimensão largura x altura
area_paredes =  2 * (4 * 3) + 2 * (5 * 3) = 24 + 30 = 54 m²

# Cada caixa de azulejos cobre 1,5 m²
area_por_caixa = 1.5

# Quantidade de caixas necessárias
num_caixas =  54 / 1.5 = 36 caixas

# Exibindo o resultado
print(f"A área total das paredes é {area_paredes:.54} metros quadrados.")
print(f"Serão necessárias {num_caixas:.36} caixas de azulejos.")
