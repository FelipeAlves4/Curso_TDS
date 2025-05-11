# A quantidade de competidores, quantidade de folhas compradas e quantas folhas será para cada competidor
quantidade_competidores = int(input("A quantidade de candidatos que terá no campeonato? "))
folhas_compradas = int(input("Qual é a quantidade de folhas compradas pela diretora? "))
folha_competidor = int(input("Qual será a quantidade de folhas para cada: "))

#quantidade folhas que irá precisar
total_necessario = quantidade_competidores * folha_competidor

#verificando se a quantidade comprada é o suficiente
if total_necessario <= folhas_compradas: 
    print("Sim a quantidade é suficiente")
else:
    print("Não, estara faltando folhas")