def backtrack(grafo, n, v, colores_asignados):
    if len(colores_asignados) == len(grafo.obtener_vertices()):
        return True

    for color in range(n):
        if all(color != colores_asignados.get(u) for u in grafo.adyacentes(v)):
            colores_asignados[v] = color
            if backtrack(grafo, n, grafo.vertice_aleatorio(), colores_asignados):
                return True
            colores_asignados.pop(v)

    return False


def backtrack(grafo, n, v, colores_asignados, visitados):
    visitados.add(v)

    if len(colores_asignados) == len(grafo.obtener_vertices()):
        return True

    for w in grafo.adyacentes(v):
        if w in visitados:
            continue
        for color in range(n):
            if color != colores_asignados.get(v):
                colores_asignados[w] = color
                if backtrack(grafo, n, w, colores_asignados, visitados):
                    return True
                colores_asignados.pop(w)

    return False


def colorear(grafo, n):
    colores_asignados = {}
    visitados = set()
    v_inicial = grafo.vertice_aleatorio()
    colores_asignados[v_inicial] = 0

    return backtrack(grafo, n, v_inicial, colores_asignados, visitados)


def es_compatible(grafo, colores, v):
    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True

def coloreo_rec(grafo, n, colores, v):
    for color in range(n):kjvñlbx{flkxk,m}
        colores[v] = color
        
        if not es_compatible(grafo, colores, v):
            
        correcto = True
        for w in grafo.adyacentes(v):
            if w in colores:
                continue
            if not coloreo_rec(grafo, n, colores, w):
                correcto = False
                break
            if correcto:
                return True

        del colores[v]
        return False

def coloreo(grafo, n):
    colores = {}
    return coloreo_rec(grafo, n, colores, grafo.vertice_aleatorio())