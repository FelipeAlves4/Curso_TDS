# Dados
funcionarios = ["Func1", "Func2", "Func3"]

# Disponibilidade dos funcionários (1 = disponível, 0 = não disponível)
disponibilidade = {
    "Func1": [1],  # Disponível na semana 1
    "Func2": [1],  # Disponível na semana 1
    "Func3": [0]   # Não disponível na semana 1
}

# Competências dos funcionários (nível de habilidade)
competencias = {
    "Func1": {"Habilidade_A": 3, "Habilidade_B": 2},
    "Func2": {"Habilidade_A": 4, "Habilidade_B": 6},
    "Func3": {"Habilidade_A": 2, "Habilidade_B": 5}
}

# Necessidades do projeto
necessidades_projeto = {"Habilidade_A": 3, "Habilidade_B": 6}
necessidades_projeto2 = {"Habilidade_A": 3, "Habilidade_B": 2}


# Alocação do projeto
funcionario_alocado = None

# Verificar cada funcionário
for func in funcionarios:
    # Verifica se o funcionário está disponível
    if disponibilidade[func][0] == 1:
        # Verifica se o funcionário atende a todas as habilidades necessárias
        atende_requisitos = True
        for habilidade, nivel_requerido in necessidades_projeto.items():
            if competencias[func].get(habilidade, 0) < nivel_requerido:
                atende_requisitos = False
                break
        
        # Se o funcionário atende aos requisitos, aloca ao projeto e interrompe a busca
        if atende_requisitos:
            funcionario_alocado = func
            break

# Exibir o resultado da alocação
if funcionario_alocado:
    print(f"O funcionário {funcionario_alocado} e  foi alocado ao projeto.")
else:
    print("Nenhum funcionário atende aos requisitos do projeto.")
