def es_dominating_set(grafo, current_solution):
    visitados = set()
    for v in current_solution:
        if v not in visitados:
            visitados.add(v)
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
    return len(grafo) == len(visitados)


def dominating_set_bck(grafo, sol_actual, mejor_solucion):

    if es_dominating_set(grafo, sol_actual) and len(sol_actual) < len(mejor_solucion):
        mejor_solucion[:] = sol_actual[:]
        return

    if len(sol_actual) >= len(mejor_solucion) and not es_dominating_set(grafo, sol_actual):
        return

    for v in grafo:
        if v not in sol_actual:
            sol_actual.append(v)
            dominating_set_bck(grafo, sol_actual, mejor_solucion)
            sol_actual.pop()

def dominating_set_min(grafo):

    mejor_solucion = grafo.obtener_vertices()

    dominating_set_bck(grafo, [], mejor_solucion)

    return mejor_solucion