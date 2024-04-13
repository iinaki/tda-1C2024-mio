# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. Indicar y justificar la complejidad del algoritmo implementado.

# Definición:

# n = 0 --> Debe devolver 1
# n = 1 --> Debe devolver 1
# n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    anterior = 0
    actual = 1

    for i in range(2,n + 1):
        nuevo = actual + anterior
        anterior = actual
        actual = nuevo

    return actual

def fibonacci(n):
    M_FIB = [None] * (n + 1)

    M_FIB[0] = 0
    M_FIB[1] = 1

    for i in range(2,n + 1):
        M_FIB[i] = M_FIB[i - 1] + M_FIB[i - 2]

    return M_FIB[n]