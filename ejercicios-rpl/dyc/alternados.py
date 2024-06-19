# Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}
# Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

def merge_alternate(arr, l, m, r):
    n = (r - l + 1) // 2
    temp = [0] * (2 * n)
    for i in range(n):
        temp[2 * i] = arr[l + i]
        temp[2 * i + 1] = arr[l + n + i]
    arr[l:r + 1] = temp

def alternar_rec(arr, l, r):
    if r - l + 1 <= 2:
        return
    m = (l + r) // 2
    alternar_rec(arr, l, m)
    alternar_rec(arr, m + 1, r)
    merge_alternate(arr, l, m, r)

def alternar(arr):
    alternar_rec(arr, 0, len(arr) - 1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(alternar(arr))