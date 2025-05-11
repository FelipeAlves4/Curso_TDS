# Função para verificar se o pedido de férias pode ser aprovado
def verificar_ferias(tempo_servico, mes_ferias):
    # Verifica se o funcionário tem mais de 3 anos de serviço
    if tempo_servico >= 3:
        return "Pedido de férias aprovado."
    
    # Funcionários com menos de 3 anos de serviço
    temporada_alta = [1, 6, 7, 12]  # Meses de alta temporada
    if mes_ferias in temporada_alta:
        return "Pedido de férias negado. Funcionários com menos de 3 anos não podem tirar férias na alta temporada."
    else:
        return "Pedido de férias aprovado."

# Entrada de dados do usuário
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))
mes_ferias = int(input("Digite o mês desejado para tirar férias (1-12): "))

# Verifica se o pedido pode ser aprovado
resultado = verificar_ferias(tempo_servico, mes_ferias)
print(resultado)