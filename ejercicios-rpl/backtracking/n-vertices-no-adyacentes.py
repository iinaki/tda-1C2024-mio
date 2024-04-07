# Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

# 'Devolver una lista con los n vértices, o None de no ser posible'

def backtrack(grafo, v, seleccionados, n):
    if len(seleccionados) == n:
        return seleccionados

    for w in grafo.obtener_vertices():
        if w not in seleccionados and all(not grafo.estan_unidos(w, u) for u in seleccionados):
            seleccionados.append(w)
            resultado = backtrack(grafo, v, seleccionados, n)
            if resultado:
                return resultado
            seleccionados.remove(w)

    return None

def no_adyacentes(grafo, n):
    for v in grafo.obtener_vertices():
        seleccionados = [v]
        resultado = backtrack(grafo, v, seleccionados, n)
        if resultado:
            return resultado

    return None


