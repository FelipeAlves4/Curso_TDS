"""import random

# Configuração dos tabuleiros vazios
tamanho_tabuleiro = 10
tabuleiro_jogador = [["~"] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]
tabuleiro_computador = [["~"] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]
tabuleiro_ataques = [["~"] * tamanho_tabuleiro for _ in range(tamanho_tabuleiro)]

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

# Função para posicionar os navios aleatoriamente
def posicionar_navios(tabuleiro, num_navios):
    navios = []
    while len(navios) < num_navios:
        x = random.randint(0, tamanho_tabuleiro - 1)
        y = random.randint(0, tamanho_tabuleiro - 1)
        if tabuleiro[x][y] == "~":
            tabuleiro[x][y] = "N"
            navios.append((x, y))
    return navios

# Posicionar 3 navios para cada jogador
navios_jogador = posicionar_navios(tabuleiro_jogador, 3)
navios_computador = posicionar_navios(tabuleiro_computador, 3)

# Função para realizar um ataque em uma posição
def realizar_ataque(x, y, tabuleiro, navios):
    if (x, y) in navios:
        tabuleiro[x][y] = "X"  # Acerto
        print("Acertou um navio!")
        return True
    else:
        tabuleiro[x][y] = "O"  # Erro
        print("Água!")
        return False

# Função principal do jogo
def batalha_naval():
    rodadas = 0
    while True:
        print("\nSeu tabuleiro:")
        imprimir_tabuleiro(tabuleiro_jogador)
        print("\nTabuleiro de ataques:")
        imprimir_tabuleiro(tabuleiro_ataques)
        
        # Jogador escolhe a posição de ataque
        x = int(input("Escolha uma linha (0-4): "))
        y = int(input("Escolha uma coluna (0-4): "))
        
        # Jogador ataca o tabuleiro do computador
        if realizar_ataque(x, y, tabuleiro_computador, navios_computador):
            tabuleiro_ataques[x][y] = "X"
            navios_computador.remove((x, y))
        else:
            tabuleiro_ataques[x][y] = "O"
        
        # Verifica se o jogador venceu
        if not navios_computador:
            print("Parabéns, você venceu!")
            break
        
        # Computador ataca aleatoriamente
        x_comp = random.randint(0, tamanho_tabuleiro - 1)
        y_comp = random.randint(0, tamanho_tabuleiro - 1)
        print(f"O computador ataca a posição ({x_comp}, {y_comp})")
        
        if realizar_ataque(x_comp, y_comp, tabuleiro_jogador, navios_jogador):
            navios_jogador.remove((x_comp, y_comp))
        
        # Verifica se o computador venceu
        if not navios_jogador:
            print("O computador venceu!")
            break
        
        rodadas += 1

# Inicia o jogo
batalha_naval()
"""
