# Criando um vetor para armazenar os valores de Fibonacci até Fib(60)
fib = [0] * 61
fib[0] = 0
fib[1] = 1

# Preenchendo o vetor com os valores de Fibonacci
for i in range(2, 61):
    fib[i] = fib[i-1] + fib[i-2]

# Lendo o número de casos de teste
T = int(input())

# Processando cada caso de teste
for _ in range(T):
    N = int(input())
    # Imprimindo o resultado
    print(f"Fib({N}) = {fib[N]}")
