
# def encontrar_indice_mas_bajo(alumnos, pos_izq, pos_der):
#     if pos_izq == pos_der:
#         return pos_izq

#     medio = (pos_izq + pos_der) // 2

#     if alumnos[medio] < alumnos[medio-1]:
#         return medio

#     indice_mas_bajo_izq = encontrar_indice_mas_bajo(alumnos, pos_izq, medio)
#     indice_mas_bajo_der = encontrar_indice_mas_bajo(alumnos, medio+1, pos_der)

#     if alumnos[indice_mas_bajo_izq] < alumnos[indice_mas_bajo_der]:
#         return indice_mas_bajo_izq
#     return indice_mas_bajo_der

# int fun(int[] A, int i, int j)
# ------------------------------
#  if i == j then
#   | return i
#  else
#   | int m = floor((i+j)/2)
#   | if A[m-1] > A[m] < A[m+1] then
#   |  | return m
#   | else if A[m] > A[m+1] then
#   |  | return fun(A, m+1, j)
#   | else
#   |  | return fun(A, i, m-1)

def encontrar_indice_mas_bajo(alumnos, pos_izq, pos_der):
    if pos_izq == pos_der:
        return pos_izq

    medio = (pos_izq + pos_der) // 2

    if alumnos[medio-1] > alumnos[medio] < alumnos[medio+1]:
        return medio

    if alumnos[medio] > alumnos[medio+1]:
        return encontrar_indice_mas_bajo(alumnos, medio+1, pos_der)

    return encontrar_indice_mas_bajo(alumnos, pos_izq, medio-1)


def indice_mas_bajo(alumnos):
    return encontrar_indice_mas_bajo(alumnos, 0, len(alumnos) - 1)

alumnos = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23]
alumnos2 = [5,4,1,9,0,6,4,1]
print(alumnos[indice_mas_bajo(alumnos)])  # DEBERIA DAR 0.98
print(alumnos2[indice_mas_bajo(alumnos2)])