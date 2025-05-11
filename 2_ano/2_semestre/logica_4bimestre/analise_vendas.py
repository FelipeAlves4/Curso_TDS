# vendas mensais, a soma das vendas e no final a media das vendas
vendas_mensais = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
vendas_anual = sum(vendas_mensais)
print(f"A suas vendas anuais são {vendas_anual}")
media_vendas = vendas_anual / len(vendas_mensais)
print(f"A media das vendas é {media_vendas}")


#Max -> máximo daquele vetor
#indez -> posição daquele vetor

maximo = vendas_mensais.index(max(vendas_mensais)) + 1 #Irá pegar a posição do mes que houve mais vendas e o 1 será para de vez o vetor começar no 0 irá ser 1
print(f"O mes que teve mais vendas foi {maximo}º e o maximo de vendas foi {max(vendas_mensais)}")

