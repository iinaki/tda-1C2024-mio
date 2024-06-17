
def backtrack(g1, g2, vertices_g1, vertices_g2, mapping, used):
    if len(mapping) == len(vertices_g1):
        return True

    v1 = vertices_g1[len(mapping)]

    for v2 in vertices_g2:
        if v2 in used:
            continue

        mapping[v1] = v2
        used.add(v2)

        if es_valido(mapping):
            if backtrack(mapping, used):
                return True

        del mapping[v1] 
        used.remove(v2)

    return False

# Verificar si la asignación parcial es válida
def es_valido(g1, g2, mapping):
    for v1 in mapping:
        for w1 in g1.adyacentes(v1):
            if w1 in mapping:
                v2 = mapping[v1]
                w2 = mapping[w1]
                if not g2.estan_unidos(v2, w2) or g1.peso_arista(v1, w1) != g2.peso_arista(v2, w2):
                    return False

    es_valido = False
    for v1 in mapping:
        v2 = mapping[v1]
        if len(g1.adyacentes(v1)) == len(g2.adyacentes(v2)):
            es_valido = True
            break

    return es_valido

def son_isomorfos(g1, g2):
    if len(g1.obtener_vertices()) != len(g2.obtener_vertices()):
        return False

    # Generar una lista de vértices de ambos grafos
    vertices_g1 = list(g1.obtener_vertices())
    vertices_g2 = list(g2.obtener_vertices())

    return backtrack(g1, g2, vertices_g1, vertices_g2, {}, set())

def hay_isomorfismo(g1, g2):
    return False