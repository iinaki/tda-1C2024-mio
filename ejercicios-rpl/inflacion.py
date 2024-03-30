def precios_inflacion(R):
    R.sort(reverse=True)
    precio_min_final = 0

    for j, r in enumerate(R):
        precio_min_final = precio_min_final + r**(j+1)

    return precio_min_final