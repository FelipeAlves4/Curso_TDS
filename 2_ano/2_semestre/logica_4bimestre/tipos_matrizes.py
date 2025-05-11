matriz_quadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz_quadrada[2][1])

matriz_quadrada[2][1] = 10 
print(matriz_quadrada[2][1])

matriz = [
    [30,43,8],
    [25,33,99],
    [90,21,1]
]

linha = len(matriz_quadrada)
coluna = len(matriz_quadrada[0])
matriz_soma = [[0 for _ in range(linha)] for _ in range(coluna)]


for i in range(linha):
    for j in range(coluna):
        matriz_soma[i][j] = matriz_quadrada[i][j] + matriz[i][j]
        
print(matriz_soma)

matriz_subtracao = [[0 for _ in range(linha)] for _ in range(coluna)]

for i in range(linha):
    for j in range(coluna):
        matriz_subtracao[i][j] = matriz_quadrada[i][j] - matriz[i][j]
        
print(matriz_subtracao)
        