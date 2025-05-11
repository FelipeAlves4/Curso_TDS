# Criando a classe Carros para poder puxar os dados dela
class Carros:
    def __init__(self, marca, ano, modelo, cor, preco):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    # Puxando as informações
    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_modelo(self):
        return self.modelo

    def get_cor(self):
        return self.cor

    def get_preco(self):
        return self.preco

    # Definindo métodos para atualizar os valores
    def set_novamarca(self, nova_marca):
        self.marca = nova_marca

    def set_ano(self, ano_novo):
        self.ano = ano_novo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def set_preco(self, novo_preco):
        self.preco = novo_preco

# Classe Estoque para gerenciar o estoque de carros
class Estoque:
    def __init__(self):
        self.__carros = []  # Criar lista para os carros

    def adicionar_carro(self, carro):
        self.__carros.append(carro)
        print(f"Carro: {carro.get_marca()}, ano: {carro.get_ano()}, modelo: {carro.get_modelo()}, cor: {carro.get_cor()}, preço: {carro.get_preco()} adicionado ao estoque.")

    def listar_carros(self):
        if not self.__carros:
            print("O estoque está vazio.")
        else:
            for i, carro in enumerate(self.__carros, start=1):
                print(f"{i}. {carro.get_marca()} {carro.get_modelo()} - Ano: {carro.get_ano()} - Cor: {carro.get_cor()} - Preço: R${carro.get_preco():.2f}")

# Definindo as variáveis
carro1 = Carros("Toyota", 2020, "Corolla", "Preto", 85000.00)
carro2 = Carros("Honda", 2018, "Civic", "Azul Marinho", 90000.00)
carro3 = Carros("Ford", 2015, "Focus", "Vermelho", 75000.00)

estoque = Estoque()
estoque.adicionar_carro(carro1)
estoque.adicionar_carro(carro2)
estoque.adicionar_carro(carro3)

# Listando os carros em estoque
estoque.listar_carros()

# Alterando as informações
carro1.set_novamarca("Fiat")
carro2.set_ano(2020)
carro1.set_modelo("Fiat Uno")
carro3.set_cor("Azul")
carro2.set_preco(20000.0)

# Listando os carros em estoque após as alterações
estoque.listar_carros()