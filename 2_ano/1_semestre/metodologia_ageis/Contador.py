class Contador:    
    def __init__(self):
        self._valor = 0
    def aumentar (self):         #defindo metodo para acrescentar mais 1 
        self._valor += 1
    def diminuir(self):           #defindo metodo para diminuir o valor 
        self._valor -= 1
    def get(self):            #defindo metodo para puxar o valor 
        return self._valor

contar = Contador()
contar.aumentar()
contar.aumentar()
print(contar.get())
contar.diminuir()
print(contar.get())
