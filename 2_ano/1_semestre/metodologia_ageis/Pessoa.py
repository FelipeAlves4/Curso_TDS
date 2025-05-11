class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def get(self):
        return self.nome
    

pessoa1 = Pessoa("Cleiton", "20")
print(pessoa1.get.nome())
