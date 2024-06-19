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

# HACEMOS CON JUAN EL VAGO

def juan_el_vago(trabajos):
    n = len(trabajos)

    # DINAMICA
    if n == 0:
        return []

    dp = [0] * n
    dp[0] = trabajos[0]

    for i in range(1, n):
        dp[i] = max(trabajos[i] + (dp[i - 2] if i >= 2 else 0), dp[i - 1])

    # RECONSTRUCCION
    dias_trabajo = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            dias_trabajo.append(i)
            i -= 2
        else:
            i -= 1

    dias_trabajo.reverse()
    return dias_trabajo

def lunatico(ganancias):
    if len(ganancias) == 0:
        return []

    if len(ganancias) == 1:
        return [0]
        
    casas_no_circular = juan_el_vago(ganancias)
    if (casas_no_circular[0] == 0 and casas_no_circular[-1] != len(ganancias) - 1) or (casas_no_circular[0] != 0 and casas_no_circular[-1] == len(ganancias) - 1) or (casas_no_circular[0] != 0 and casas_no_circular[-1] != len(ganancias) - 1):
        return casas_no_circular

    ganancias_sin_ultima = ganancias[:-1]
    ganancias_sin_primera = ganancias[1:]

    casas_sin_ultima = juan_el_vago(ganancias_sin_ultima)
    casas_sin_primera = juan_el_vago(ganancias_sin_primera)
    casas_sin_primera = [i + 1 for i in casas_sin_primera]

    ganancias_sin_ultima = sum([ganancias[i] for i in casas_sin_ultima])
    ganancias_sin_primera = sum([ganancias[i] for i in casas_sin_primera])

    if ganancias_sin_ultima > ganancias_sin_primera:
        return casas_sin_ultima
    else:
        return casas_sin_primera
    
