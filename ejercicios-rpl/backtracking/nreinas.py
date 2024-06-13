from grafo import Grafo

def ajedrez(n):
    def posiciones_adyacentes(i, j, n):
        adyacentes = []
        # Movimientos horizontales y verticales
        for k in range(n):
            if k != i:
                adyacentes.append((k, j))
            if k != j:
                adyacentes.append((i, k))
        
        # Movimientos diagonales
        for k in range(1, n):
            if i + k < n and j + k < n:
                adyacentes.append((i + k, j + k))
            if i + k < n and j - k >= 0:
                adyacentes.append((i + k, j - k))
            if i - k >= 0 and j + k < n:
                adyacentes.append((i - k, j + k))
            if i - k >= 0 and j - k >= 0:
                adyacentes.append((i - k, j - k))
        
        return adyacentes

    grafo = Grafo()
    
    # Agregar vértices
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))
    
    # Agregar aristas
    for i in range(n):
        for j in range(n):
            adyacentes = posiciones_adyacentes(i, j, n)
            for adyacente in adyacentes:
                if grafo.estan_unidos((i, j),adyacente):
                    continue
                grafo.agregar_arista((i, j), adyacente)
    
    return grafo

def es_compatible( grafo , puestos ):
    for v in puestos :
        for w in puestos :
            if v == w: continue
            if grafo.estan_unidos(v , w):
                return False
    return True

def _ubicacion_BT( grafo , vertices , v_actual , puestos , n ):
    if v_actual == len(vertices) :
        return False
    if len ( puestos ) == n :
        return es_compatible( grafo , puestos )

    if not es_compatible( grafo , puestos ):
        return False

    puestos.add( vertices[ v_actual ])

    if _ubicacion_BT( grafo , vertices , v_actual + 1 , puestos , n):
        return True

    puestos.remove( vertices [ v_actual ])

    return _ubicacion_BT( grafo , vertices , v_actual + 1, puestos , n)

def nreinas(n):
    if n == 0:
        return []

    if n == 1:
        return [(0,0)]

    grafo = ajedrez(n)
    vertices = grafo.obtener_vertices()
    puestos = set()
    _ubicacion_BT(grafo, vertices, 0, puestos, n)

    return list(puestos)
