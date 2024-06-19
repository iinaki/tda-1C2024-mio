# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista.

def max_crossing_subarray(arr, l, m, r):
    suma_izquierda = float('-inf')
    suma_temp = 0
    max_izq_ind = m

    for i in range(m, l - 1, -1):
        suma_temp += arr[i]
        if suma_temp > suma_izquierda:
            suma_izquierda = suma_temp
            max_izq_ind = i

    suma_derecha = float('-inf')
    suma_temp = 0
    max_der_ind = m + 1

    for i in range(m + 1, r + 1):
        suma_temp += arr[i]
        if suma_temp > suma_derecha:
            suma_derecha = suma_temp
            max_der_ind = i

    return (suma_izquierda + suma_derecha, max_izq_ind, max_der_ind)

def max_subarray_rec(arr, l, r):
    if l == r:
        return (arr[l], l, r)

    m = (l + r) // 2

    suma_izquierda, izq_ini, izq_fin = max_subarray_rec(arr, l, m)
    suma_derecha, der_ini, der_fin = max_subarray_rec(arr, m + 1, r)
    suma_cruzada, cruz_ini, cruz_fin = max_crossing_subarray(arr, l, m, r)

    if suma_izquierda >= suma_derecha and suma_izquierda >= suma_cruzada:
        return (suma_izquierda, izq_ini, izq_fin)
    elif suma_derecha >= suma_izquierda and suma_derecha >= suma_cruzada:
        return (suma_derecha, der_ini, der_fin)
    else:
        return (suma_cruzada, cruz_ini, cruz_fin)

def max_subarray(arr):
    if not arr:
        return []
    suma_maxima, inicio, fin = max_subarray_rec(arr, 0, len(arr) - 1)
    return arr[inicio:fin + 1]