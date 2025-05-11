class Usuario:
    def __init__(self,nome,senha):
        self.__nome = nome
        self.__senha = senha
    def alterar_senha(self,senha_nova):
        self.__senha = senha_nova
    def acessar_conta(self):
        return f"Sua conta é {self.__nome} e {self.__senha}"

pessoa = Usuario("Rogerio", "Construtor")
pessoa.alterar_senha("Construtor213")
print(pessoa.acessar_conta())