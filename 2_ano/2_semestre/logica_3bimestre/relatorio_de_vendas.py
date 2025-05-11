# Dados simulados de vendas diárias para cada produto
vendas_diarias = [
    ("Produto A", [120, 130, 115, 140, 150, 110, 135]),
    ("Produto B", [200, 180, 220, 210, 205, 190, 195]),
    ("Produto C", [95, 100, 105, 100, 110, 95, 98]),
    ("Produto D", [320, 310, 300, 315, 330, 310, 325])
]

# Dicionário para armazenar os totais de vendas
totais_vendas = {}
medias_vendas = {}

# Processar os dados de vendas diárias
for produto, vendas in vendas_diarias:
    total = sum(vendas)
    media = total / len(vendas)
    
    # Armazenar os totais e médias no dicionário
    totais_vendas[produto] = total
    medias_vendas[produto] = media

# Exibir o relatório de vendas
print("Relatório de Vendas:")
for produto in totais_vendas:
    print(f"{produto}:")
    print(f"  Total de vendas: {totais_vendas[produto]}")
    print(f"  Média de vendas diárias: {medias_vendas[produto]:.2f}")
