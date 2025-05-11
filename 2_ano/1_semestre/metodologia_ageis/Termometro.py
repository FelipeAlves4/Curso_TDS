class Termometro:
    def __init__(self, temperatura=0):
        self.__temperatura_celsius = temperatura

    def get_temperatura_fahrenheit(self):
        return (self.__temperatura_celsius * 9/5) + 32

    def set_temperatura_fahrenheit(self, temperatura_f):
        self.__temperatura_celsius = (temperatura_f - 32) * 5/9

    def get_temperatura_celsius(self):
        return self.__temperatura_celsius

    def set_temperatura_celsius(self, temperatura_c):
        self.__temperatura_celsius = temperatura_c

# Uso da classe
termometro = Termometro()
termometro.set_temperatura_fahrenheit(68)
print(termometro.get_temperatura_fahrenheit())  # Deve mostrar 68
print(termometro.get_temperatura_celsius())  # Deve mostrar 20.0 (equivalente a 68°F)
