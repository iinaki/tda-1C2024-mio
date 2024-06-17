
def sol_trivial(elementos, w):
    for e in elementos:
        if e < w:
            return [e]
    return []

def mochila_bck(elementos, i, w, sol_actual, mejor_sol):
    if sum(e for e in sol_actual) > w :
        return

    if sum(e for e in sol_actual) > sum(e for e in mejor_sol):
        mejor_sol[:] = sol_actual[:]

    for i in range(i, len(elementos)):
        sol_actual.append(elementos[i])
        mochila_bck(elementos, i + 1, w, sol_actual, mejor_sol)
        sol_actual.pop()

def mochila(P, w):
    sol_actual = []
    mejor_sol = sol_trivial(P, w)

    mochila_bck(P, 0, w, sol_actual, mejor_sol)
    return mejor_sol

def max_grupos_bodegon(P, W):
    return mochila(P, W)