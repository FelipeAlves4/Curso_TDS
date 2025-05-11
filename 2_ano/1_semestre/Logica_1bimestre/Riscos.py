riscos = int(input("Qual risco vc gostaria, Operacional,Financeiro,Mercado? ")).upper()

if riscos == 'operacional':
    print("Você escolheu o risco Operacional, Sistema identificado")
elif riscos == 'financeiro':
    print("Vc escolheu o Financeiro, Sistema identificado")
elif riscos == 'mercado':
    print("Vc escolheu o de Mercado, Sistema identificado")
else:
    print("SISTEMA N IDENTIFICADO")
