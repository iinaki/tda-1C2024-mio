def sol_trivial(grafo):
    return [v for v in grafo]


def count_of_vertices(grafo):
    count = 0
    for v in grafo:
        for _ in grafo.adyacentes(v):
            count += 1
    return count // 2


def es_solucion_vertex_cover(grafo, sol):
    count = 0
    visited = set()
    for v in sol:
        for w in grafo.adyacentes(v):
            if v != w and (v, w) not in visited:
                visited.add((v, w))
                visited.add((w, v))
                count += 1
    return count == count_of_vertices(grafo)


def es_mejor_solucion(grafo, sol, mejor_sol):
    return es_solucion_vertex_cover(grafo, sol) and len(sol) < len(mejor_sol)

def vertex_cover_min_bck(grafo, i, solucion_actual, mejor_sol):

    if es_mejor_solucion(grafo, solucion_actual, mejor_sol):
        mejor_sol[:] = solucion_actual[:]
        return

    if i == len(grafo) or len(solucion_actual) >= len(mejor_sol):
        return

    for v in grafo:
        if v not in solucion_actual:
            solucion_actual.append(v)
            vertex_cover_min_bck(grafo, i + 1, solucion_actual, mejor_sol)
            solucion_actual.pop()

def vertex_cover_min(grafo):
    if len(grafo) == 0:
        return []

    count = count_of_vertices(grafo)
    primera_sol = sol_trivial(grafo)
    mejor_sol = primera_sol[:]

    vertex_cover_min_bck(grafo, 0, [], mejor_sol)

    return mejor_sol