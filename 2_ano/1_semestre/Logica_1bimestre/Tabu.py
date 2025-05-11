max_tabu = 5
max_numeros = 10 
tabuada = 1 

while  tabuada <= max_tabu:
    print(f"Tabuado do {tabuada}")

    numero = 1
    while numero <= max_numeros:
        produto = tabuada * numero
        print(f"{tabuada} * {numero} = {produto}")
        numero += 1 
    tabuada += 1
    print()