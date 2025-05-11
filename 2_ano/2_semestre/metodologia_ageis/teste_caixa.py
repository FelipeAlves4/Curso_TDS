valor_total = 0
qtd = int(input("Quantidade de peças compradas: "))

for i in range(qtd):
    valor = float(input("Qual o valor do produto: "))
    valor_total += valor

if qtd < 6:
    print(f"Você comprou {qtd} peças, logo não terá desconto.")
elif qtd > 5 and qtd < 10:
    print(f"Você comprou {qtd} peças, logo terá 10% de desconto. ")
    print(f"O Seu desconto será de R$ {valor_total*0.1}, logo o seu valor será {valor_total * 0.9}")
elif qtd > 10:
    print((f"Você comprou {qtd} peças, logo terá 20% de desconto."))
    print(f"O Seu desconto será de R$ {valor_total*0.2}, logo o seu valor será {valor_total * 0.8}")