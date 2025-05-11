depa = input("Qual seu departamento? ").strip().lower()

if depa == "software":
    print("Recomendo laptops com alto desempenho.")
elif depa == "marketing":
    print("Recomendo tablets para facilitar a apresentação e mobilidade.")
elif depa == "recursos humanos":
    print("Recomendo computadores desktop devido à sua estabilidade e custo-benefício.")
else:
    print("Recomendo equipamentos com especificações de última geração.")
