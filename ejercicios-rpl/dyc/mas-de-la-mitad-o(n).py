# Implementar una función (que utilice división y conquista) de orden O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces.

def mas_de_la_mitad_rec(arr, l, r):
    if l == r:
        return arr[l]
    m = (l + r) // 2
    left = mas_de_la_mitad_rec(arr, l, m)
    right = mas_de_la_mitad_rec(arr, m + 1, r)
    if left == right:
        return left
    left_count = sum(1 for i in range(l, r + 1) if arr[i] == left)
    right_count = sum(1 for i in range(l, r + 1) if arr[i] == right)
    return left if left_count > right_count else right

def mas_de_la_mitad(arr):
    n = len(arr)
    mayoritario = mas_de_la_mitad_rec(arr, 0, n - 1)
    return sum(1 for i in range(n) if arr[i] == mayoritario) > n // 2
