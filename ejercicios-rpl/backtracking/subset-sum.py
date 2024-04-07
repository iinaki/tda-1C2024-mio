def subset_sum(L, index, n, solucion_parcial, soluciones):
	# Si encuentro una solucion la agrego a las soluciones
	if sum(solucion_parcial) == n:
		soluciones.append(solucion_parcial[:])
		return
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or index >= len(L):
		return

	solucion_parcial.append(L[index])
	subset_sum(L, index+1, n, solucion_parcial, soluciones)
	solucion_parcial.pop()

	subset_sum(L, index+1, n, solucion_parcial, soluciones)
	return
