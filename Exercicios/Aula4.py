# Entrada de dados
codigo = int(input("Informe o código de origem do produto: "))

# Verificação da região de procedência
if codigo == 1:
    regiao = "Região Sul"
elif codigo == 2:
    regiao = "Região Norte"
elif codigo == 3:
    regiao = "Região Leste"
elif codigo == 4:
    regiao = "Região Oeste"
elif codigo == 5 or codigo == 6:
    regiao = "Região Nordeste"
elif codigo in [7, 8, 9]:
    regiao = "Região Sudeste"
elif codigo == 10:
    regiao = "Região Centro-oeste"
elif codigo == 11:
    regiao = "Região Noroeste"
else:
    regiao = "Importado"

# Exibindo o resultado
print(f"O produto é da {regiao}.")
