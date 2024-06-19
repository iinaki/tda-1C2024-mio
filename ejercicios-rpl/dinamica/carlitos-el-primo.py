# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi. Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos.

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

# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    return mochila(c_publicitaria, P)