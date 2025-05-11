class Livro:
    def __init__(self,titulo,autor,ano): 
        self.titulo = titulo
        self.autor = autor 
        self.ano = ano 

class Biblioteca:
    def __init__ (self): 
        self.livros = []  #ele irá se referenciar na classe Livro
    def adicionar_livro(self,livro):
        self.livros.append(livro) #irá adicionar os Livros da classe acima  a uma lista vazia no self livros
    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo}, {livro.autor}, {livro.ano}")
        
#usando as classes
bi = Biblioteca()
bi.adicionar_livro(Livro("One piece","Oda",1997))
bi.adicionar_livro(Livro("Dom casmurro","Machado de Assis",1989))
bi.adicionar_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954))
    
bi.listar_livros()


