qualidade_ar = int(input("Qual a qualidade do ar (0-100): "))

if qualidade_ar > 80:
    print("Qualidade do ar excelente. Mantenha as políticas atuais")
elif qualidade_ar > 60 and qualidade_ar < 80:
    print("Qualidade do ar boa. Considere políticas moderadas de melhoria")
else:
    print("Qualidade do ar ruim. Implementar políticas rigorosas de melhoria")