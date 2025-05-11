# a pessoa escolhe o numero aleatorio para a sequencia
numero = int(input("digite um numero: "))

# sequencia do numero escolhido
for i in range(1, numero + 1):
   # primeira linha 
   print(i, i**2, i**3)
   # segunda linha 
   print(i, i**2 + 1, i**3 + 1 )