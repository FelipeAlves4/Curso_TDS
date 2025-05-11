"""matriz = [[1]*3 for _ in range(4)]
print(matriz)


identidade = [[1 if i==j else 0 for j in range(3)] for i in range(3)]
print(identidade)

"""

# Matriz de adjacência representando as conexões
connections = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0]
]

# Função para encontrar amigos em comum e sugerir novas conexões
def recommend_friends(connections):
    n = len(connections)
    recommendations = []
    
    for i in range(n):
        for j in range(n):
            if i != j and connections[i][j] == 0: # Sem conexão direta
                common_friends = sum(a and b for a, b in zip(connections[i], connections[j]))
            
                if common_friends > 0:
                    recommendations.append((f"U{i+1}", f"U{j+1}", common_friends))
                    
    # Ordenar recomendações por número de amigos em comum, em ordem decrescente

    recommendations.sort(key=lambda x: x[2], reverse=True)
    return recommendations
# Executar a função e imprimir as recomendações
new_friend_suggestions = recommend_friends(connections)
for suggestion in new_friend_suggestions:
    print(f"Usuários {suggestion[0]} e {suggestion[1]} têm {suggestion[2]} amigos em comum. Considerar conectar!")
