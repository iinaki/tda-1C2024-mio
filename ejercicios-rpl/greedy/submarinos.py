# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    if len(matriz) == 0:
        return []
    
    filas = len(matriz)
    columnas = len(matriz[0])
    submarinos_posiciones = [(i, j) for i in range(filas) for j in range(columnas) if matriz[i][j]]
    
    # Lista para almacenar las posiciones de los faros
    faros = []
    
    # Matriz para mantener el estado de cobertura de cada celda
    cubierto = [[False] * columnas for _ in range(filas)]
    
    # Función para marcar las celdas cubiertas por un faro en la posición (x, y)
    def marcar_cobertura(x, y):
        for i in range(max(0, x-2), min(filas, x+3)):
            for j in range(max(0, y-2), min(columnas, y+3)):
                cubierto[i][j] = True
    
    # Función para verificar si un submarino en (x, y) está cubierto
    def esta_cubierto(x, y):
        return cubierto[x][y]
    
    # Colocar los faros
    for x, y in submarinos_posiciones:
        if not esta_cubierto(x, y):
            # Colocar un faro en (x, y) y marcar la cobertura
            faros.append((x, y))
            marcar_cobertura(x, y)
    
    return faros