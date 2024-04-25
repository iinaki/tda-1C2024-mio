# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa
# se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

# 1. Creamos un arreglo dp de tamaño n para almacenar la ganancia máxima obtenible hasta la casa i.
# 2. Inicializamos dp[0] = g[0] y dp[1] = max(g[0], g[1]) para las dos primeras casas.
# 3. Para cada casa i desde la tercera hasta la penúltima, calculamos dp[i] como el máximo entre robar la casa i y la casa i-2 o no robar la casa i (tomando la ganancia acumulada hasta la casa i-1).
# 4. Para la última casa, tomamos la ganancia máxima entre robarla y no robarla.
# 5. La ganancia máxima obtenible será el máximo valor en el arreglo dp.

# La ecuación de recurrencia para este problema, teniendo en cuenta la circularidad de las casas, es la siguiente:

# \[ dp[i] = \begin{cases} 
#       g[0] & \text{si } i = 0 \\
#       \max(g[0], g[1]) & \text{si } i = 1 \\
#       \max(dp[i-2] + g[i], dp[i-1]) & \text{si } 1 < i < n-1 \\
#       \max(dp[i-2] + g[i], dp[i-1], dp[0]) & \text{si } i = n-1
#    \end{cases}
# \]

# Esta ecuación representa cómo se calcula la ganancia máxima obtenible al robar cada casa, considerando la circularidad de la calle.

def construir_G(ganancias, n):
    G = [0] * n
    G[0] = ganancias[0]
    G[1] = max(ganancias[0], ganancias[1])

    for i in range(2, n - 1):
        G[i] = max(ganancias[i] + G[i - 2], G[i - 1])

    # i == n-1:
    print("EN LA ULTIMA CASA ganancias[i] + G[i - 2] es", ganancias[i] + G[i - 2] - G[0], "y G[i - 1] es", G[i - 1], "y G[0] es", G[0])
    # si inicialmente agarre la casa 0, y la ultima casa es la n-1, entonces la ultima casa no la puedo agarrar
    G[n-1] = max(ganancias[i] + G[i - 2] , G[i - 1], G[0])
    
    return G

    # ME COMBIENE EMPEZAR A LA DERECHA O A LA IZQUIERDA?


# def construir_G(ganancias, n):
#     G = [0] * n

#     for i in range(n):
#         if i == 0:
#             opt_casa_anterior = ganancias[n - 1]
#             opt_casa_anteanterior = ganancias[n - 2]
#         elif i == 1:
#             opt_casa_anterior = G[0]
#             opt_casa_anteanterior = ganancias[n - 1]
#         else:
#             opt_casa_anterior = G[i - 1]
#             opt_casa_anteanterior = G[i - 2]

#         valor_actual = ganancias[i]

#         G[i] = max(valor_actual + opt_casa_anteanterior, opt_casa_anterior)
    
#     return G


def lunatico(ganancias):
    n = len(ganancias)

    if n == 0:
        return []
    if n == 1:
        return [0]

    G = construir_G(ganancias, n)

    print(G)
    soluciones = []
    d = n-1
    while(d >= 0):
        opt_casa_anterior = G[d - 1] if d > 0 else 0
        opt_casa_anteanterior = G[d - 2] if d > 1 else 0

        valor_actual = ganancias[d]

        # if valor_actual + opt_casa_anteanterior > opt_casa_anterior:
        #     print("Robar casa", d)
        #     soluciones.append(d)
        #     d -= 2
        # else:
        #     d -= 1
        if d == 0 or G[d] != G[d - 1]:
            print("Robar casa", d)
            if d == 0:
                if soluciones[0] == n-1:
                    soluciones.append(d)
                    break

            soluciones.append(d)
            d -= 2
        else:
            d -= 1

    soluciones.reverse()

    return soluciones

# tests

test1 = [100, 20, 30, 70, 50]
print(lunatico(test1)) # [1, 4]

test2 = [100, 20, 30, 70, 50, 100]
print(lunatico(test2)) # [1, 3, 6]
