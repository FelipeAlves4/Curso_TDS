from random import randint

cp = randint(1,50)
jogador = int(input("Digite seu palpite: "))
print("Lembrando, vc tem apenas 5 tentativas dps dessa")
tentativas = 0
max_tentativas = 5

while  max_tentativas > tentativas:
    if cp > jogador: 
        print("Seu chute foi baixo")
        tentativas = tentativas +1
    elif cp < jogador:
        print("Seu chute foi alto dms")
        tentativas = tentativas + 1
    elif cp == jogador:
     print("parabens!! vc ganhou")
     print(cp)
     break
    jogador = int(input("Digite seu palpite: "))

else: 
    print(f"Vc exedeu o numero maximo de tentativas, o numero secreto erá {cp}")