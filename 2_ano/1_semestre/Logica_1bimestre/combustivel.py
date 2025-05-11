# Função principal do programa
def calcular_litros_necessarios(tempo, velocidade):
    # Calcula a distância percorrida
    distancia = tempo * velocidade
    
    # Calcula os litros necessários
    litros_necessarios = distancia / 12
    
    # Retorna o resultado com 3 casas decimais
    return f"{litros_necessarios:.3f}"

# Leitura dos valores de entrada
tempo = int(input("Digite o tempo gasto na viagem (em horas): "))
velocidade = int(input("Digite a velocidade média durante a viagem (em km/h): "))

# Calcula e imprime a quantidade de litros necessária
litros_necessarios = calcular_litros_necessarios(tempo, velocidade)
print(f"Quantidade de litros necessária: {litros_necessarios}")
