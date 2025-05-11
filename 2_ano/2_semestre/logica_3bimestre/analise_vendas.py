# Função para coletar e exibir o inventário
def gerenciar_inventario():
    inventario = []
    
    # Solicitar ao usuário quantos itens ele deseja adicionar
    num_itens = int(input("Quantos itens deseja adicionar ao inventário? "))

    # Iterar pelo número de itens e coletar os dados de cada um
    for i in range(num_itens):
        print(f"\nInserindo item {i + 1}:")
        nome = input("Nome do equipamento: ")
        categoria = input("Categoria do equipamento: ")
        quantidade = int(input("Quantidade do equipamento: "))
        
        # Armazenar o item como um dicionário e adicioná-lo à lista
        item = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        }
        inventario.append(item)

    # Exibir o inventário completo
    print("\n==== Inventário Completo ====")
    for item in inventario:
        print(f"Nome: {item['nome']}, Categoria: {item['categoria']}, Quantidade: {item['quantidade']}")
        
# Executar a função de gerenciamento de inventário
gerenciar_inventario()