    # Leitura do valor inicial
V = int(input())

# Inicialização do vetor com 10 posições
N = [0] * 10

# Coloca o valor lido na primeira posição e duplica nas seguintes
for i in range(10):
    if i == 0:
        N[i] = V
    else:
        N[i] = N[i - 1] * 2

# Exibe cada posição do vetor com o formato pedido
for i in range(10):
    print(f"N[{i}] = {N[i]}")
