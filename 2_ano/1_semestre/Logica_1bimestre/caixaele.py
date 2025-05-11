dinheiro = int(input("Digite o valor que deseja sacar: "))
notas_50 = 0 
notas_20 = 0
notas_10 = 0 
notas_5 = 0 

while dinheiro >= 50:
    dinheiro -= 50 
    notas_50 += 1 
while dinheiro >= 20:
    dinheiro -= 20 
    notas_20 += 1 
while dinheiro >= 10:
    dinheiro -= 10 
    notas_10 += 1
while dinheiro >= 5:
    dinheiro -= 5
    notas_5 += 1 

print(f"Notas de R$50,00 {notas_50} notas ")
print(f"Notas de R$20,00 {notas_20} notas")
print(f"Notas de R$10,00 {notas_10} notas")
print(f"Notas de R$5,00 {notas_5} notas")
