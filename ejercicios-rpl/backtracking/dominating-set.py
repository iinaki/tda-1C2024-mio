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

# OTRA SOLUCION

def es_dom_set(grafo, dom_set):
    for v in grafo.obtener_vertices():
        if v not in dom_set:
            adjacent_covered = False
            for ady in grafo.adyacentes(v):
                if ady in dom_set:
                    adjacent_covered = True
                    break
            if not adjacent_covered:
                return False
    return True

def backtracking(grafo, dom_set_mejor, set_actual, vertice_actual):
    if es_dom_set(grafo, set_actual):
        if len(set_actual) < len(dom_set_mejor):
            dom_set_mejor[:] = set_actual
        return
    
    if vertice_actual == len(grafo.obtener_vertices()):
        return
    
    if len(set_actual) > len(dom_set_mejor):
        return

    set_actual.append(grafo.obtener_vertices()[vertice_actual])
    backtracking(grafo, dom_set_mejor, set_actual, vertice_actual + 1)

    set_actual.pop()
    backtracking(grafo, dom_set_mejor, set_actual, vertice_actual + 1)

def dominating_set_min(grafo):
    dom_set_mejor = grafo.obtener_vertices()
    backtracking(grafo, dom_set_mejor, [], 0)
    return dom_set_mejor