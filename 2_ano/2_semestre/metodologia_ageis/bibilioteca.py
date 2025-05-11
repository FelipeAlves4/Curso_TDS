class Livro: 
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_ano_publicacao(self):
        return self.ano_publicacao
    
    def get_preco(self):
        return self.preco
    
    def set_titulo(self, titulo_novo):
        self.titulo = titulo_novo
    
    def set_autor(self, novo_autor):
        self.autor = novo_autor
    
    def set_publicacao(self, novo_ano):
        self.ano_publicacao = novo_ano
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco

# Definindo as variáveis
titulo = input("Qual o título do livro? ")
autor = input("Qual o autor do livro? ")
ano_publicacao = int(input("Qual o ano de publicação do livro? "))
preco = float(input("Qual o preço do livro? "))
livro = Livro(titulo,autor,ano_publicacao,preco)

print(f"O ano de publicação foi {livro.get_ano_publicacao()} com um preço de {livro.get_preco()}")

# Alterando as informações 
livro.set_titulo("Piratasdo")
livro.set_autor("Felipe")
livro.set_publicacao(2015)
livro.set_preco(50.0)

print(f"O livro {livro.get_titulo()} foi escrito por {livro.get_autor()}")
print(f"O ano de publicação foi {livro.get_ano_publicacao()} com um preço de {livro.get_preco()}")
# Puxando as informações
print(f"O livro {livro.get_titulo()} foi escrito por {livro.get_autor()}")