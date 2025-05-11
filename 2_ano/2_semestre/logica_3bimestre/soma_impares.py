numero = int(input())

for i in range(1, numero+1):
    X, Y = map(int, input().split())


    soma_impares = 0 

    if X > Y: #Verfica se x é maior q y 
        X,Y = Y,X #Troca as posições para facilitar o loop
    
    # Iterar pelos números entre X e Y 
    for num in range(X + 1, Y):
        if num % 2 != 0:  # Se for ímpar
            soma_impares += num
    
    # Imprimir o resultado para o caso atual
    print(soma_impares)
    