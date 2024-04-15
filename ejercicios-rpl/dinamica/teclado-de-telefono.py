# Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

# Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
# Para N=2, depende de cuál dígito se comienza.
# Empezando por 0, son válidos 00, 08 (cantidad: 2)
# Empezando por 1, son válidos 11, 12, 14 (cantidad: 3)
# Empezando por 2, son válidos 22, 21, 23, 25 (cantidad: 4)
# Empezando por 3, son válidos 33, 32, 36 (cantidad: 3)
# Empezando por 4, son válidos 44, 41, 45, 47 (cantidad: 4)
# Empezando por 5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
# Empezando por 6, son válidos 66, 63, 65, 69 (cantidad: 4)
# Empezando por 7, son válidos 77, 74, 78 (cantidad: 3)
# Empezando por 8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
# Empezando por 9, son válidos 99, 96, 98 (cantidad: 3)

# CELULAR =>
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #

# from grafo import Grafo

# def numeros_posibles(k, n):
#     if n == 1:
#         return 1
    
#     celular = Grafo()
#     for i in range(10):
#         celular.agregar_vertice(i)
    
#     celular.agregar_arista(1, 1)
#     celular.agregar_arista(1, 2)
#     celular.agregar_arista(1, 4)

#     celular.agregar_arista(2, 2)
#     celular.agregar_arista(2, 3)
#     celular.agregar_arista(2, 5)

#     celular.agregar_arista(3, 3)
#     celular.agregar_arista(3, 6)

#     celular.agregar_arista(4, 4)
#     celular.agregar_arista(4, 5)
#     celular.agregar_arista(4, 7)

#     celular.agregar_arista(5, 5)
#     celular.agregar_arista(5, 6)
#     celular.agregar_arista(5, 8)

#     celular.agregar_arista(6, 6)
#     celular.agregar_arista(6, 9)

#     celular.agregar_arista(7, 7)
#     celular.agregar_arista(7, 8)

#     celular.agregar_arista(8, 8)
#     celular.agregar_arista(8, 9)
#     celular.agregar_arista(8, 0)

#     celular.agregar_arista(9, 9)

#     celular.agregar_arista(0, 0)

#     dp = [[0] * 10 for _ in range(n + 1)]
#     for i in range(10):
#         dp[1][i] = 1

#     for l in range(2, n + 1):
#         for d in range(10):
#             for vecino in celular.adyacentes(k):
#                 dp[l][d] += dp[l - 1][vecino]
            
#     return sum(dp[n])

def numeros_posibles1(k, n):
    if n == 1:
        return 1
    
    dp = [[0] * 10 for _ in range(n + 1)]
    
    for i in range(10):
        dp[1][i] = 1
    
    # Movimientos válidos desde cada dígito
    movimientos = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [0, 5, 7, 8, 9],
        9: [6, 8, 9]
    }
    
    for l in range(2, n + 1):
        for d in range(10):
            for vecino in movimientos[d]:
                dp[l][d] += dp[l - 1][vecino]
    print(dp)
    return dp[n][k]



print(numeros_posibles1(0, 3))