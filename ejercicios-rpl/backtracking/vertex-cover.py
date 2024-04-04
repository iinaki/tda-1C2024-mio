#Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

def vertex_cover_min(grafo):
    vertex_cover = []

    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            aristas.append((v, w))

    while aristas:
        v, w = aristas.pop()
        if v not in vertex_cover:
            vertex_cover.append(v)

        if w not in vertex_cover:
            vertex_cover.append(w)

        aristas = [(x, y) for x, y in aristas if x != v and x != w and y != v and y != w]

    return vertex_cover

def _vertex_cover_min(grafo, v, visitados, vertex_cover):
    visitados.add(v)
    vertex_cover.append(v)
    if len(visitados) == len(grafo):
        return True
    for w in grafo.adyacentes(v):
        if w not in visitados: # Esta es en sí nuestra poda
            if _vertex_cover_min(grafo, w, visitados, vertex_cover):
                return True
    visitados.remove(v)     # Permitiendo volver a venir a este vértice
    vertex_cover.pop()            # por otro camino
    return False

def vertex_cover_min(grafo):
    vertex_cover = []
    visitados = set()  
    for v in grafo:
        if _vertex_cover_min(grafo, v, visitados, vertex_cover):
            return vertex_cover
            
    return None
