def precios_deflacion(R):
    R.sort()
    precio_min_final = 0

    for j, r in enumerate(R):
        precio_min_final = precio_min_final + r/2**(j)

    return precio_min_final