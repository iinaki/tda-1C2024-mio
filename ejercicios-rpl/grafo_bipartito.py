

def isBipartite(adj, v, visited, color):

	for u in adj[v]: 
		# If vertex u is not explored before
		if (visited[u] == False):
			# Mark present vertices as visited
			visited[u] = True
			# Mark its color opposite to its parent
			color[u] = not color[v]
			# If the subtree rooted at vertex v 
			# is not bipartite
			if (not isBipartite(adj, u, visited, color)):
				return False
				
		# If two adjacent are colored with
		# same color then the graph is not 
		# bipartite
		elif (color[u] == color[v]):
			return False
	
	return True


N = 6

adj = [[] for i in range(N + 1)]

visited = [0 for i in range(N + 1)]
color = [0 for i in range(N + 1)]

visited[1] = True
color[1] = 0

isBipartite(adj, 1, visited, color)



# def pintar_grafo(grafo, rojos, azules, v_actual, color_actual):
#     adyacentes = grafo.adyacentes(v_actual)

#     if color_actual == "rojo" and any(v in rojos for v in adyacentes):
#         return False
    
#     if color_actual == "azul" and any(v in azules for v in adyacentes):
#         return False
# pintar_grafo(grafo,rojos,azules,vertices[0], "rojo")

def _es_bipartito(grafo, vertices, visitados, v_actual):
    adyacentes = grafo.adyacentes(v_actual)
    visitados.add(v_actual)

    for v in adyacentes:
        if not visitados[v]:
            color[v] = not color[v_actual]
            if not _es_bipartito(grafo, vertices, visitados, v):
                return False
        else:
            if color[v] == color[v_actual]:
                return False
    return True



def es_bipartito(grafo):
    vertices = grafo.vertices()

    visitados = {}

    #guardo tupla de vertice y color
    visitados.add((vertices[0],0))
    
    return _es_bipartito(grafo, vertices, visitados, vertices[0])
	

### DEFINITIVA
def _es_bipartito(vertice, color, visitados, colores, grafo):
        visitados.add(vertice)
        colores[vertice] = color
        
        for adyacente in grafo.adyacentes(vertice):
            if adyacente in visitados:
                if colores[adyacente] == color:
                    return False
            elif not _es_bipartito(adyacente, not color, visitados, colores, grafo):
                return False
                
        return True

def es_bipartito(grafo):   
    visitados = set()
    colores = {}
    
    for v in grafo:
        if v not in visitados and not _es_bipartito(v, False, visitados, colores, grafo):
            return False
                
    return True