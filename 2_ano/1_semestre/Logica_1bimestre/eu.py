idade = int(input("Digite sua idade: "))
exame = input("Vc deve passar por exame: (vou/nvou)").lower()
violaçao = input("Vc tem violação de transito registrada? (s/n)").lower()

if idade >= 18 and exame =='vou' and violaçao =='n':
 print("Vc pode tirar a carta de motorista!")

else:
 print("Vc n pode tirar carta de motorista!")