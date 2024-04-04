def cambio(monedas, monto):
    monedas.sort(reverse=True)
    monedas_cambio = []

    while monto > 0:
        for moneda in monedas:
            if monto - moneda >= 0:
                monto = monto - moneda
                monedas_cambio.append(moneda)
                break

    return monedas_cambio

monedas = [1, 2, 5, 10, 20, 50, 100, 200]
monto = 123
print(cambio(monedas, monto))  # [100, 20, 2, 1]