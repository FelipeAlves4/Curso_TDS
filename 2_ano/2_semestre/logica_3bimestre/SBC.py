# Lendo a quantidade de linhas
numero_linhas = int(input("Qual os intervalos de tempo? "))

# Inicializando a variável para armazenar a distância total
distancia_total = 0 

for i in range(numero_linhas):
    tempo,velocidade = map(int,input().split())
    # Calculando a distância para o intervalo atual e somando ao total
    distancia_total += tempo*velocidade

#apresentando total
print(f"total percorrido: {distancia_total}")