while True:
    N = int(input())
    if N == 0:
        break
    
    matriz = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            matriz[i][j] = min(i, j, N - 1 - i, N - 1 - j) + 1
    
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    
    print("")  # Linha em branco entre as matrizes
