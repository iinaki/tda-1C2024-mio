import pulp

def mochila_lineal(w, v, W):
    y = []

    for i in range(len(w)):
        y.append(pulp.LpVariable(f'y{i}', cat='Binary'))

    prob = pulp.LpProblem("Mochila", pulp.LpMaximize)
    prob = pulp.LpAffineExpresion([(y[i],w[i]) for i in range(len(w))]) <= W
    prob += pulp.LpAffineExpresion([(y[i],v[i]) for i in range(len(v))])

    prob.solve()
    return list(map(lambda yi: pulp.value(yi), y))

Y = mochila_lineal(pesos, valores, W)
print('Peso usado:', sum([Y[i] * pesos[i] for i in range(len(Y))]))
print('Valor obtenido:', sum([Y[i] * valores[i] for i in range(len(Y))]))