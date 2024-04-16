# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa
# se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

def construir_G(ganancias, n):
    G = [0] * n
    G[0] = ganancias[0]
    G[1] = max(ganancias[0], ganancias[1])

    for i in range(2, n):
        if i == n-1:
            print("EN LA ULTIMA CASA ganancias[i] + G[i - 2] - G[0] es", ganancias[i] + G[i - 2] - G[0], "y G[i - 1] es", G[i - 1])
            G[i] = max(ganancias[i] + G[i - 2] - G[0], G[i - 1])
        else:
            G[i] = max(ganancias[i] + G[i - 2], G[i - 1])
    
    return G


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
            soluciones.append(d)
            d -= 2
        else:
            d -= 1

    soluciones.reverse()

    return soluciones

# tests
print(lunatico([100, 20, 30, 70, 50])) # [1, 4]