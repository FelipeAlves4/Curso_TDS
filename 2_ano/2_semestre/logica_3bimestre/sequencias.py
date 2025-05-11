caso = 1

while True:
    try:
        N = int(input())
        sequencia = [0]
        
        for i in range(1, N + 1):
            sequencia.extend([i] * i)
        
        print(f"Caso {caso}: {len(sequencia)} numeros")
        print(" ".join(map(str, sequencia)))
        print("")
        
        caso += 1
        
    except EOFError:
        break
