def converter_dias(dia):
    anos = dia // 365
    dias_restantes = dia % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30
     
    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)") 
    
dia = int(input("Coloque a quantidade de dias: "))
print(converter_dias(dia))
