
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