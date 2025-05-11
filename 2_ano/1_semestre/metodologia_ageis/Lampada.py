class Lampada:        #definindo a classe Lampada
    def __init__(self):        #Criando um corpo para nossa classe
        self.estado = False                   #Começa desligada 
    def alterar(self):               #criando o metodo para ligar a Lampada   
        self.estado = not self.estado        #Ligando a Lampada
        return self.estado               

lampada = Lampada()   #variavel lampada recebe a Classe Lampada 
print(lampada.alterar()) 
print(lampada.alterar())
