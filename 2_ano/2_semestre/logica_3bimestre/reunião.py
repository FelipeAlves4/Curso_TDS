participantes = int(input("Qual é a quantidades de pessoas q irá participar da reunião? "))
reuniao = input("A reunião é normal ou executiva? ").lower()


if participantes >15 or reuniao == 'executiva':
    print("A reunião será na Sala grande")
elif participantes <= 5:
    print("A reunião será na Sala Pequena")
elif participantes >= 6 and participantes <= 15:
    print("A reunião será na Sala Média")

