def es_compatible( grafo , colores , v):
    for w in grafo.adyacentes (v):
        if w in colores and colores[w] == colores[v ]:
            return False
    return True

def _coloreo_rec( grafo , k , colores , v ):
    for color in range(k):
        colores[v] = color
        if not es_compatible( grafo , colores , v ):
            continue
        correcto = True

        for w in grafo.adyacentes (v):
            if w in colores: continue
            if not _coloreo_rec( grafo , k , colores , w) :
                correcto = False
                break

        if correcto:
            return True

    del colores[v]
    return False

def colorear( grafo , n):
    if len(grafo) == 0:
        return True
    colores = {}
    return _coloreo_rec ( grafo , n , colores , grafo.vertice_aleatorio() )