# Vetor de estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para exibir o estoque atual
def exibir_estoque(estoque):
    for i, qtd in enumerate(estoque):
        print(f"Produto {i+1}: {qtd} unidades")

# Função para atualizar o estoque após uma venda
def vender_produto(estoque, produto, quantidade_vendida):
    if estoque[produto - 1] >= quantidade_vendida:
        estoque[produto - 1] -= quantidade_vendida
    else:
        print(f"Estoque insuficiente para o Produto {produto}")

# Função para adicionar unidades ao estoque
def adicionar_estoque(estoque, produto, quantidade_adicionada):
    estoque[produto - 1] += quantidade_adicionada

# Passos experimentais

# 1. Exibir estoque inicial
print("Estoque inicial:")
exibir_estoque(estoque)

# 2. Vender 3 unidades do produto 1 e 2 unidades do produto 4
vender_produto(estoque, 1, 3)  # Produto 1, venda de 3 unidades
vender_produto(estoque, 4, 2)  # Produto 4, venda de 2 unidades

# 3. Adicionar 10 unidades ao produto 5
adicionar_estoque(estoque, 5, 10)

# 4. Exibir estoque atualizado
print("\nEstoque atualizado:")
exibir_estoque(estoque)
