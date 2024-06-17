def subset_sum(L, i, n, solucion_parcial, soluciones):
	# Si encuentro una solucion la agrego a las soluciones
	if sum(solucion_parcial) == n:
		soluciones.append(solucion_parcial[:])
		return
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or i >= len(L):
		return

	solucion_parcial.append(L[i])
	subset_sum(L, i+1, n, solucion_parcial, soluciones)
	solucion_parcial.pop()

	subset_sum(L, i+1, n, solucion_parcial, soluciones)
	return

def sumatorias_n(lista, n):
	soluciones = []
	subset_sum(lista,0,n,[],soluciones)
	return soluciones


def subset_sum_modif(L, i, n, solucion_parcial, soluciones, todas_soluciones):
	if sum(solucion_parcial) <= n:
		todas_soluciones.append(solucion_parcial[:])

	# Si encuentro una solucion la agrego a las soluciones
	if sum(solucion_parcial) == n:
		soluciones.append(solucion_parcial[:])
		return
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or i >= len(L):
		return

	solucion_parcial.append(L[i])
	subset_sum_modif(L, i+1, n, solucion_parcial, soluciones, todas_soluciones)
	solucion_parcial.pop()

	subset_sum_modif(L, i+1, n, solucion_parcial, soluciones, todas_soluciones)
	return

def max_sumatoria_n(lista, n):
    soluciones = []
    todas_soluciones = []
    subset_sum_modif(lista,0,n,[],soluciones, todas_soluciones)

    if len(soluciones) > 0:
        return soluciones[0]
    else:
        max_suma = max(map(sum, todas_soluciones))
        max_suma_soluciones = [sol for sol in todas_soluciones if sum(sol) == max_suma]
        return max_suma_soluciones[0]

