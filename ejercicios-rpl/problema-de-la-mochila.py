# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "con un algoritmo Greedy". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción


# cada elemento i de la forma (valor, peso)
# ORDENAR POR VALOR / PESO
def mochila(elementos, W):
    elementos.sort(key=lambda x: x[0]/x[1], reverse=True)
    elementos_mochila = []

    for elemento in elementos:
        if W - elemento[1] >= 0:
            elementos_mochila.append(elemento)
            W = W - elemento[1]

    return elementos_mochila