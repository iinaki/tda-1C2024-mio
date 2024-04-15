# Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

# Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.


# def laberinto(matriz):
#     n = len(matriz)
#     m = len(matriz[0])
    
#     dp = [0] * n
#     dp[0] = matriz[0][0]
#     i = 1

#     while i < n:
#         dp[i] = max(matriz[i] + (dp[i - 2] if i >= 2 else 0), dp[i - 1])

#     return dp.pop()

def laberinto(matriz):
    if not matriz:
        return 0
    
    N, M = len(matriz), len(matriz[0])
    dp = [[0] * M for _ in range(N)]
    
    dp[0][0] = matriz[0][0]
    
    # Llenar la primera fila
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]
    
    # Llenar la primera columna
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]
    
    # Llenar el resto de la matriz
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = matriz[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    print(dp)
    return dp[N - 1][M - 1]

# Ejemplo de uso
matriz = [
    [3, 7, 9, 2],
    [2, 8, 3, 5],
    [5, 9, 4, 1],
    [6, 3, 8, 2]
]

print("Ganancia máxima:", laberinto(matriz))

