# Classe base para todos os produtos eletrônicos
class ProdutoEletronico:
    def __init__(self, nome, marca, preco):
        # Inicializando os atributos comuns a todos os produtos eletrônicos
        self.nome = nome
        self.marca = marca
        self.preco = preco

    # Método para exibir as informações do produto
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Marca: {self.marca}, Preço: R${self.preco:.2f}")

# Subclasse para smartphones
class Smartphone(ProdutoEletronico):
    def __init__(self, nome, marca, preco, capacidade_armazenamento):
        # Inicializando a classe base
        super().__init__(nome, marca, preco)
        # Atributo específico para smartphones
        self.capacidade_armazenamento = capacidade_armazenamento

    # Sobrescrevendo o método exibir_informacoes para incluir o armazenamento
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Capacidade de Armazenamento: {self.capacidade_armazenamento}GB")

# Subclasse para laptops
class Laptop(ProdutoEletronico):
    def __init__(self, nome, marca, preco, memoria_ram):
        # Inicializando a classe base
        super().__init__(nome, marca, preco)
        # Atributo específico para laptops
        self.memoria_ram = memoria_ram

    # Sobrescrevendo o método exibir_informacoes para incluir a memória RAM
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Memória RAM: {self.memoria_ram}GB")

# Subclasse para televisores
class Televisor(ProdutoEletronico):
    def __init__(self, nome, marca, preco, tamanho_tela):
        # Inicializando a classe base
        super().__init__(nome, marca, preco)
        # Atributo específico para televisores
        self.tamanho_tela = tamanho_tela

    # Sobrescrevendo o método exibir_informacoes para incluir o tamanho da tela
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho da Tela: {self.tamanho_tela} polegadas")

# Exemplo de testes práticos
if __name__ == "__main__":
    # Criando instâncias de cada tipo de produto
    smartphone = Smartphone("iPhone 12", "Apple", 5999.99, 128)
    laptop = Laptop("MacBook Air", "Apple", 8499.99, 16)
    televisor = Televisor("Smart TV", "Samsung", 2999.99, 55)

    # Exibindo as informações de cada produto
    print("Informações do Smartphone:")
    smartphone.exibir_informacoes()
    print("\nInformações do Laptop:")
    laptop.exibir_informacoes()
    print("\nInformações da Televisão:")
    televisor.exibir_informacoes()