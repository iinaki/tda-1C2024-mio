# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.

def bolsas(capacidad, productos):
    productos.sort()
    bolsas_usadas = []
    bolsa_actual = []

    capacidad_actual = 0

    for producto in productos:
        if producto + capacidad_actual <= capacidad:
            bolsa_actual.append(producto)
            capacidad_actual += producto
        else:
            bolsas_usadas.append(bolsa_actual)
            bolsa_actual = [producto]
            capacidad_actual = producto

    if bolsa_actual:
        bolsas_usadas.append(bolsa_actual)

    return bolsas_usadas