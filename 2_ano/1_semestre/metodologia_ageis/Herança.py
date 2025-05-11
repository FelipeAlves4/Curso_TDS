class Veiculo:
    def acelerar(self):
        raise NotImplementedError("Metodo acelerar a ser implementado")
    
class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando")

class Moto(Veiculo):
    def acelerar(self):
        print("Moto acelerando potencia maxima")
    
carro = Carro()
moto = Moto()
carro.acelerar()
moto.acelerar()