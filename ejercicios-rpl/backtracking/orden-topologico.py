from grafo import Grafo

def es_ciclo(grafo, v, visitado, pila):
    visitado[v] = True
    pila[v] = True

    for vecino in grafo.adyacentes(v):
        if not visitado[vecino]:
            if es_ciclo(grafo, vecino, visitado, pila):
                return True
        elif pila[vecino]:
            return True

    pila[v] = False
    return False

def tiene_ciclo(grafo):
    visitado = {v: False for v in grafo.obtener_vertices()}
    pila = {v: False for v in grafo.obtener_vertices()}

    for v in grafo.obtener_vertices():
        if not visitado[v]:
            if es_ciclo(grafo, v, visitado, pila):
                return True
    return False

def backtracking(grafo, visitado, orden, resultados):
    if len(orden) == len(grafo.obtener_vertices()):
        resultados[0] += 1
        return

    for v in grafo.obtener_vertices():
        if not visitado[v] and all(visitado[vecino] for vecino in grafo.adyacentes(v)):
            visitado[v] = True
            orden.append(v)
            backtracking(grafo, visitado, orden, resultados)
            orden.pop()
            visitado[v] = False

def contar_ordenamientos(grafo):
    if tiene_ciclo(grafo):
        return 0

    visitado = {v: False for v in grafo.obtener_vertices()}
    resultados = [0]
    backtracking(grafo, visitado, [], resultados)
    return resultados[0]