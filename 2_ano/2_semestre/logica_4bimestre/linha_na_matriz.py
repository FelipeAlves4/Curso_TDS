# Leitura do número da linha e da operação
L = int(input())
T = input().strip()

# Criação da matriz 12x12 com os valores fornecidos
M = []
for i in range(12):
    row = []
    for j in range(12):
        row.append(float(input()))
    M.append(row)

# Realizar a operação na linha L
# Se a operação for 'S', faz a soma; se for 'M', calcula a média
if T == 'S':
    resultado = sum(M[L])
elif T == 'M':
    resultado = sum(M[L]) / 12

# Imprimir o resultado com uma casa decimal
print(f"{resultado:.1f}")
