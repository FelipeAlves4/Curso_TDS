
# Matriz de temperatura original (3 cidades ao longo de 4 meses)
matriz_temperatura = [
    [22,25,28,32],  # Cidade 1
    [20,23,26,30],  # Cidade 2
    [18,22,25,29]   # Cidade 3
]

matriz_transposta = []

#Transpondo a matriz
for i in range(len(matriz_temperatura[0])): #Total de colunas
    linha_transposta = []
    for j in range(len(matriz_temperatura)): #Total de linhas
        linha_transposta.append(matriz_temperatura[j][i])
    
    matriz_transposta.append(linha_transposta)
    
print(matriz_transposta)