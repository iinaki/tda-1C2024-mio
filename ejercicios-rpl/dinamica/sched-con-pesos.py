# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción


# def construir_p(charlas):
#     p = [0] * (len(charlas))
#     for j in range(1, len(charlas)):
#         for i in range(j, -1, -1):
#             if charlas[i][1] <= charlas[j][0]:
#                 p[j] = i
#                 break
#     return p

def construir_p(charlas):
    n = len(charlas)
    p = [0] * (n + 1)
    p[0] = 0

    for j in range(1, n+1):
        i = j - 1
        while i >= 0 and charlas[i][1] > charlas[j-1][0]:
            i -= 1
        p[j] = i + 1
    return p


def sched_con_pesos(charlas):
    charlas.sort(key=lambda x: x[1])
    n = len(charlas)
    M_SCHE = [0] * (n+1)
    p = construir_p(charlas)
    print("P ES:")
    print(p)
    charlas = [(0, 0, 0)] + charlas
    print("CHARLAS ES:", charlas)

    for j in range(1, n+1):
        M_SCHE[j] = max(charlas[j][2] + M_SCHE[p[j]], M_SCHE[j - 1])

    print("M_SCHE ES:")
    print(M_SCHE)

    return M_SCHE, p, charlas

def sched_solucion(M_SCHE, charlas, p, j, solucion):
    if j == 0:
        if charlas[j][1] <= solucion[len(solucion) - 1][0]:
            solucion.append(charlas[j])
        return solucion
    if charlas[j][2] + M_SCHE[p[j]] >= M_SCHE[j - 1]:
        solucion.append(charlas[j])
        return sched_solucion(M_SCHE, charlas, p, p[j], solucion)
    else:
        return sched_solucion(M_SCHE, charlas, p, j - 1, solucion)

def scheduling(charlas):
    if len(charlas) == 0:
        return []

    M_SCHE, p, charlas = sched_con_pesos(charlas)
    solucion = []

    sol = sched_solucion(M_SCHE, charlas, p, len(charlas) - 1, solucion)
    sol = sol[::-1]
    sol = sol[1:]

    return sol

# Test
charlas = [(1, 3, 5), (2, 4, 1), (3, 5, 7), (4, 6, 8), (5, 7, 9)]
charlas2 = [(1, 6, 2), (4, 8, 5), (9, 11, 4), (11, 12, 1), (14, 16, 2), (16, 17, 4)]
charlas3 = [(1, 6, 2), (7, 11, 4), (3, 14, 7), (11, 16, 2)]
# p deberia ser [0,1,0,2]

print(scheduling(charlas))
print(scheduling(charlas2))
print(scheduling(charlas3))
