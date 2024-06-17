from grafo import Grafo

def es_compatible( grafo , colores , v):
    for w in grafo.adyacentes (v):
        if w in colores and colores[w] == colores[v]:
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
    return _coloreo_rec( grafo , n , colores , grafo.vertice_aleatorio() )

def pintar_colectivos(colectivos, paradas):
    if len(colectivos) == 0:
        return 0

    if len(paradas) == 0:
        return 1

    grafo = Grafo()
    for colectivo in colectivos:
        grafo.agregar_vertice(colectivo)
    
    for parada in paradas:
        for i in range(len(parada)):
            for j in range(len(parada)):
                if i != j and not grafo.estan_unidos(parada[i], parada[j]):
                    grafo.agregar_arista(parada[i], parada[j])

    for i in range(1, len(colectivos) + 1):
        if colorear(grafo, i):
            return i
    
    return len(colectivos)
    