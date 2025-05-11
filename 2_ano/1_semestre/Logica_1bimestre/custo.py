custo = float(input("Qual é o valor da implementação? R$"))
impacto = int(input("Qual o impacto esperado? (0-10) "))

if custo < 50.000 and impacto >= 7:
    print("é viavel")
else:
    print("Política classificada como Análise Adicional Necessária")
    
