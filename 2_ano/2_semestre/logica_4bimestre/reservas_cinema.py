# Matriz de assentos (5 fileiras, 8 assentos por fileira)
assentos = [[0 for _ in range(8)] for _ in range(5)]

# Função para exibir o mapa atual dos assentos
def exibir_assentos(assentos):
    print("Mapa atual de assentos:")
    for i, fileira in enumerate(assentos):
        print(f"Fileira {i+1}: {fileira}")

# Função para reservar um assento
def reservar_assento(assentos, fileira, assento):
    if assentos[fileira-1][assento-1] == 0:
        assentos[fileira-1][assento-1] = 1
        print(f"Assento ({fileira}, {assento}) reservado com sucesso.")
    else:
        print(f"Assento ({fileira}, {assento}) já está reservado.")

# Função para cancelar a reserva de um assento
def cancelar_reserva(assentos, fileira, assento):
    if assentos[fileira-1][assento-1] == 1:
        assentos[fileira-1][assento-1] = 0
        print(f"Reserva do assento ({fileira}, {assento}) cancelada com sucesso.")
    else:
        print(f"Assento ({fileira}, {assento}) não está reservado.")

# Passos experimentais

# 1. Exibir o mapa inicial de assentos
exibir_assentos(assentos)

# 2. Reservar os assentos (1,3), (2,5) e (4,7)
reservar_assento(assentos, 1, 3)
reservar_assento(assentos, 2, 5)
reservar_assento(assentos, 4, 7)

# 3. Cancelar a reserva do assento (2,5)
cancelar_reserva(assentos, 2, 5)

# 4. Exibir o mapa atualizado de assentos
print("\nMapa atualizado de assentos:")
exibir_assentos(assentos)
