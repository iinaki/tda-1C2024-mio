from grafo import Grafo

def camino_hamilt_dfs(grafo, v, camino, visitados):
    visitados.add(v)
    camino.append(v)

    if len(visitados) == len(grafo):
        return True

    for w in grafo.adyacentes(v):
        if w not in visitados:
            if camino_hamilt_dfs(grafo, w, camino, visitados):
                return True

    visitados.remove(v)
    camino.pop()
    return False

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()

    for v in grafo:
        if camino_hamilt_dfs(grafo, v, camino, visitados):
            return camino
    
    return None