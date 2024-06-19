def mochila_dinamica(valor, peso, n, w):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if peso[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - peso[i - 1]] + valor[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp

def mochila(elementos, W):
    n = len(elementos)
    valor = [elem[0] for elem in elementos]
    peso = [elem[1] for elem in elementos]
    
    dp = mochila_dinamica(valor, peso, n, W)
    
    res = []
    w = W
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  
            res.append(elementos[i-1])
            w -= peso[i-1]  
    
    res.reverse()  
    return res

def subset_sum(elementos, v):
    n = len(elementos)
    valor = [elem for elem in elementos]
    peso = [elem for elem in elementos]
    
    elementos = [(valor[i], peso[i]) for i in range(n)]

    rta = mochila(elementos, v)
    rta = list(map(lambda x: x[0], rta))

    return rta

# OTRA SOLUCION

def subset_sum(elementos, v):
    opt = [[0]*(len(elementos)+1) for _ in range(v+1)]
    # valores -> i
    # elementos -> j
    for i in range(1, len(opt)):
        for j in range(1, len(opt[i])):
            if elementos[j-1] <= i:
                opt[i][j] = max(opt[i][j-1], elementos[j-1] + opt[i-elementos[j-1]][j-1])
            else:
                opt[i][j] = opt[i][j-1]

# mi óptimo va a ser, el max entre, no usar el elemento (me quedo con el resultado de los elementos anteriores, menos ese) o usarlo y buscar el óptimo de un valor más chico y sin ese elemento

    # reconstruccion
    solucion = []
    i = v
    j = len(elementos)
    while i > 0 and j > 0:
        if opt[i][j] != opt[i][j-1]:
            solucion.append(elementos[j-1])
            i -= elementos[j-1]
        j -= 1

    return list(reversed(solucion))

# la forma del problema es que su dificultad aumenta, a más valor y más elementos.
