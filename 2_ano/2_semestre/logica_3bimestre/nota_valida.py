validas = 0  # Contador para notas válidas
soma = 0.0   # Acumulador para a soma das notas válidas

while validas < 2:
    nota = float(input())  # Lê uma nota (número real)
    
    if 0 <= nota <= 10: #Verifica se nota é maior ou igual a zero e se maior ou igual a 10
        soma += nota       # Soma a nota válida
        validas += 1       # Conta a nota como válida
    else:
        print("nota inválida")  # Imprime a mensagem para nota inválida

# Calcula e imprime a média
media = soma / 2
print(f"média = {media:.2f}")
