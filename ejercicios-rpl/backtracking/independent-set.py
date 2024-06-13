def es_compatible( grafo , puestos ):
    for v in puestos :
        for w in puestos :
            if v == w: continue
            if grafo.estan_unidos(v , w):
                return False
    return True

def _ubicacion_BT( grafo , vertices , v_actual , puestos , n ):
    
    if len ( puestos ) == n :
        return es_compatible( grafo , puestos )
        
    if v_actual == len(vertices) :
        return False

    if not es_compatible( grafo , puestos ):
        return False

    puestos.add( vertices[ v_actual ])

    if _ubicacion_BT( grafo , vertices , v_actual + 1 , puestos , n):
        return True

    puestos.remove( vertices [ v_actual ])

    return _ubicacion_BT( grafo , vertices , v_actual + 1, puestos , n)

def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    puestos = set()
    n = len(vertices)
    while not _ubicacion_BT(grafo, vertices, 0, puestos, n) and n > 0:
        n -= 1
        puestos = set()

    return list(puestos)