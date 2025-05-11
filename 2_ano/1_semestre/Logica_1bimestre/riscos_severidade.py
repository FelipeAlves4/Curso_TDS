severidade = int(input("Coloque a severidade do risco? (1 a 5) "))
probalidade = int(input("Coloque a probalidade do risco? (1 a 5) "))

if severidade > 3 and probalidade > 3 :
    print("Risco de alta prioridade ")
elif severidade > 3 or probalidade > 3:
    print("Risco de media prioridade ")
else:
    print("Risco de baixa prioridade")