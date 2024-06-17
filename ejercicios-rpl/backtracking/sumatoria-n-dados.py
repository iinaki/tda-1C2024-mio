MIN_DADO = 1
MAX_DADO = 6

def suma_dados(solucion_parcial, n, cant_faltan, s, soluciones):    
    if sum(solucion_parcial) == s and cant_faltan == 0:
        soluciones.append(solucion_parcial[:])
        return
    
    if sum(solucion_parcial) + cant_faltan * MIN_DADO > s: return
    if sum(solucion_parcial) + cant_faltan * MAX_DADO < s: return
    
    for valor in range(MIN_DADO, MAX_DADO + 1):
        solucion_parcial.append(valor)
        suma_dados(solucion_parcial, n, cant_faltan - 1, s, soluciones)
        solucion_parcial.pop()
    return

def sumatoria_dados(n, s):
    soluciones = []
    suma_dados([], n, n, s, soluciones)
    return soluciones