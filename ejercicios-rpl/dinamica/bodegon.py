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

def bodegon_dinamico(P, W):

    P = [(p, p) for p in P]

    return mochila(P, W)

# OTRA SOLUCION

def reconstruir_solucion(p, w, optimos):
	solucion = []
	i = len(p)
	j = w

	while j > 0 and i > 0:
		if j >= p[i - 1] and optimos[i-1][j - p[i - 1]] + p[i - 1] == optimos[i][j]:
			solucion.insert(0, p[i - 1]) 
			j -= p[i - 1]  
		i -= 1 
	
	return solucion

def bodegon_dinamico(P, W):
	p = [grupo for grupo in P if grupo <= W] # filtro los grupos exedentes 
 				# (no importa modificar el indice xq se devuelven los grupos)
	w = W
	optimos = [[0 for _ in range(w+1)] for _ in range(len(p) + 1)]
	
	for i in range(1, len(p) + 1):
		for j in range(1, w + 1):
			if j >= p[i - 1]:
				optimos[i][j] = \
					max(optimos[i-1][j], optimos[i-1][j - p[i - 1]] + p[i - 1])
			else:	
				optimos[i][j] = optimos[i-1][j]

	return reconstruir_solucion(p,w, optimos)