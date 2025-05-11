def Acesso():
    cargo.lower()
    
    if cargo == 'gerente':
        print("Acesso liberado")
    elif cargo == 'funcionario' and dias_uteis == 'sabado' or dias_uteis == 'domingo':
        print("Acesso negado")
    elif cargo == 'analista' and dias_uteis == 'sabado' or dias_uteis == 'domingo':
        print("Acesso negado")
    else:
        print("Acesso liberado")

cargo = input("Qual o seu cargo?")
dias_uteis = input("Que dia ultil é hoje? ")

ponto = Acesso()
print(ponto)