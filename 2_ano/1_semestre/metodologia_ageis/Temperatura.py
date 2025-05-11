class SensorTemperatura:
    def __init__ (self,temperatura=0):
        self.__temperatura = temperatura

    
    def set_novo(self,nova_temperatura):
        if -50 <= nova_temperatura <= 150:
            self.__temperatura = nova_temperatura
        else:
            f"fora do intervalo"
    
    def puxartemp(self):
        return self.__temperatura

sensor = SensorTemperatura()
sensor.set_novo(70)
print(sensor.puxartemp())

