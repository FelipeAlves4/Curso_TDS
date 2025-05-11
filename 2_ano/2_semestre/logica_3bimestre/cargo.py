cargo = input("Qual o seu cargo? ").upper()
dia = input("Qual o dia da semana? ").upper()

if cargo == "estagiario" or cargo == "analista":
    if dia == "sabado" or dia =="domingo":
        print("Você tem o dia de folga, ent acesso negado")
    
    else:
        print("Acesso permitido")


if cargo == "gerente":
    print("Acesso permitido")