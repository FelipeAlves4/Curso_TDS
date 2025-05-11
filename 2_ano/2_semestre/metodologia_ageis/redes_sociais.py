class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.curtidas = 0
    
    def aparecer(self):
        return f"Olá, eu sou {self.nome}, tenho {self.idade} anos."
    
    def curtir(self):
        self.curtidas += 1

    def ver_curtidas(self):
        return f"minhas curtidas {self.curtidas}"

usuario = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
perfil = Perfil(usuario, idade)

print(perfil.aparecer())

perfil.curtir()
perfil.curtir()

# Para ver as curtidas, adicione parênteses ao método
print(perfil.ver_curtidas())  # Aqui você verá o número de curtidas

perfil.curtir()
print(perfil.ver_curtidas())  # Verá o número de curtidas novamente após curtir mais uma vez
