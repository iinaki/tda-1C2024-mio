def suma_dados(suma, cant_faltan, solucion_parcial, soluciones):
    if sum(solucion_parcial) == suma and cant_faltan == 0:
        soluciones.append(list(solucion_parcial))
        return
	
	if cant_faltan == 0 or sum(solucion_parcial) > n: return
    if sum(solucion_parcial) + cant_faltan*MIN_DADO > suma: return
    if sum(solucion_parcial) + cant_faltan*MAX_DADO < suma: return

    for valor in range(MIN_DADO, MAX_DADO+1):
        solucion_parcial.append(valor)
        suma_dados(suma, cant_faltan-1, solucion_parcial, soluciones)
        solucion_parcial.pop()
    return
