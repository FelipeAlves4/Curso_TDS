def pedidos():
    valor_pedido = float(input("Digite o valor do pedido: "))
    dias_para_entrega = int(input("Qual o prazo para entrega? "))

    if valor_pedido > 500 or dias_para_entrega < 4:
        print("Pedido urgente, logo vamos entregar, o mais rapido possivel!")
    elif valor_pedido >= 100 and valor_pedido <= 500 or dias_para_entrega >=4 and dias_para_entrega <= 7:
        print("Pedido Prioritário, logo vamos entregar")   
    else:
        print("Pedido normal, logo enviaremos para o correio")

pedidos()