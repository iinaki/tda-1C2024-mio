# EJ 3 FECHA 5 BUCHWALD
# Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
# (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
# algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.


def cutting_rope(n):
    if n == 1 or n == 2:
        return n
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        actual_max = 0
        for j in range(1, i):
            local_max = max(j * (i - j), j * dp[i - j])
            if local_max > actual_max:
                actual_max = local_max
        dp[i] = actual_max
    return dp


def problema_soga(n):
    OPT = [0 for _ in range(n + 1)]
    OPT[1] = 1
    OPT[2] = 1
    for i in range(3, n + 1):
        maximo = 0
        for j in range(1, i):
            maximo_local = max(j * (i - j), j * OPT[i - j],OPT[j] * (i-j) , OPT[j] * OPT[i - j])
            if maximo_local > maximo:
                maximo = maximo_local

        OPT[i] = maximo
    
    return OPT[n]
