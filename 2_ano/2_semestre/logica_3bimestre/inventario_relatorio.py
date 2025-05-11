# Função para exibir o inventário completo
def exibir_inventario(inventario):
    print("\nInventário Completo:")
    for item in inventario:
        print(f"Nome: {item['nome']}, Categoria: {item['categoria']}, Quantidade: {item['quantidade']}")
    print()  # linha em branco para melhor formatação

# Função principal para adicionar itens ao inventário
def gerenciar_inventario():
    # Solicita a quantidade de itens a serem inseridos no inventário
    qtd_itens = int(input("Quantos itens deseja adicionar ao inventário? "))

    # Lista para armazenar os itens do inventário
    inventario = []

    # Coleta as informações de cada item
    for i in range(qtd_itens):
        print(f"\nInserindo o item {i+1}:")
        nome = input("Nome do equipamento: ")
        categoria = input("Categoria do equipamento: ")
        quantidade = int(input("Quantidade: "))

        # Adiciona o item ao inventário (como um dicionário)
        item = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        }
        inventario.append(item)

    # Exibe o inventário completo após a inserção dos itens
    exibir_inventario(inventario)

# Executa o programa
gerenciar_inventario()
