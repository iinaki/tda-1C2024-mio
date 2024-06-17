
def todos_cubiertos(matriz, submarinos, faros_puestos):
    for x, y in submarinos:
        if not any(abs(x - fx) <= 2 and abs(y - fy) <= 2 for fx, fy in faros_puestos):
            return False
    return True

def backtracking(matriz, submarinos, index, faros_puestos, mejor_solucion):
    if todos_cubiertos(matriz, submarinos, faros_puestos):
        if len(faros_puestos) < mejor_solucion[0]:
            mejor_solucion[0] = len(faros_puestos)
            mejor_solucion[1] = faros_puestos[:]
        return

    if index >= len(submarinos):
        return

    x, y = submarinos[index]

    for i in range(-2, 3):
        for j in range(-2, 3):
            nx, ny = x + i, y + j
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]):
                faros_puestos.append((nx, ny))
                backtracking(matriz, submarinos, index + 1, faros_puestos, mejor_solucion)
                faros_puestos.pop()
    
    backtracking(matriz, submarinos, index + 1, faros_puestos, mejor_solucion)

def submarinos(matriz):
    submarinos = [(x, y) for x in range(len(matriz)) for y in range(len(matriz[0])) if matriz[x][y]]
    mejor_solucion = [len(submarinos), []]
    faros_puestos = []
    backtracking(matriz, submarinos, 0, faros_puestos, mejor_solucion)
    return mejor_solucion[0]

matriz = [
    [True, False, False, True, False, False],
    [False, False, True, False, False, False],
    [True, False, False, True, False, False],
    [False, True, False, False, False, False],
    [False, True, False, False, False, False],
    [False, True, False, False, False, False]
]

cantidad_minima_de_faroles, posiciones_de_faroles = submarinos(matriz)
print(f"Cantidad mínima de faros: {cantidad_minima_de_faroles}")
print(f"Posiciones de los faros: {posiciones_de_faroles}")
