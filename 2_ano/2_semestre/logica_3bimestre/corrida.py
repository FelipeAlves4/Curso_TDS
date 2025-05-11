# Quantidade que a pessoa quer correr e o tamanho da pista que irá correr 
correr,tamanho = map(int,input("Qual é a quantidade q vai correr e tamanho da pista: ").split())

# local onde a garra será colocada, o ponto especifico
ponto_termino = correr % tamanho

print(f"Ponto onde a garrafa ficará {ponto_termino}")
