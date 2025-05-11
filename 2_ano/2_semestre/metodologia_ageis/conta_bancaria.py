class CalculadoraTarifas:
    @staticmethod
    def calcular_tarifa_base():
        return 5

    @staticmethod
    def calcular_tarifa_transacao(numero_transacoes):
        if numero_transacoes > 10:
            return (numero_transacoes - 10) * 1.5
        else:
            return 0

    @staticmethod
    def calcular_tarifa_saldo(saldo):
        if saldo < 1000:
            return 10
        else:
            return 0


class ContaBancaria:
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        self.__numero_conta = numero_conta
        self.__saldo = saldo
        self.__numero_transacoes = numero_transacoes

    def get_numero_conta(self):
        return self.__numero_conta

    def get_saldo(self):
        return self.__saldo

    def get_numero_transacoes(self):
        return self.__numero_transacoes

    def depositar(self, valor):
        self.__saldo += valor
        self.__numero_transacoes += 1

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__numero_transacoes += 1
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self.__saldo:
            self.sacar(valor)  # Saca o valor da conta de origem
            conta_destino.depositar(valor)  # Deposita o valor na conta de destino
            print(f"Transferência de R${valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente para realizar a transferência.")

    def calcular_tarifa(self):
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.__numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo(self.__saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo


class ContaUniversitaria(ContaBancaria):
    def calcular_tarifa(self):
        return 0


# Exemplo de uso para testar o método de transferência
conta1 = ContaBancaria(numero_conta=123, saldo=1000)
conta2 = ContaBancaria(numero_conta=456, saldo=500)

print(f"Saldo inicial da conta 1: R${conta1.get_saldo()}")
print(f"Saldo inicial da conta 2: R${conta2.get_saldo()}")

# Realizando a transferência
conta1.transferir(300, conta2)

print(f"Saldo final da conta 1: R${conta1.get_saldo()}")
print(f"Saldo final da conta 2: R${conta2.get_saldo()}")
