def reconstruir_solucion(opt, monedas):
    monto = len(opt) - 1
    solucion = []

    while monto > 0:
        for moneda in reversed(monedas):
            if moneda <= monto and opt[monto] == 1 + opt[monto - moneda]:
                solucion.append(moneda)
                monto -= moneda

    return solucion

def cambio(monedas, monto):
    cant = [0] * (monto + 1)

    for i in range(1, monto + 1):
        minimo = i
        for moneda in monedas:
            if moneda > i:
                continue
            cantidad = 1 + cant[i - moneda]
            if cantidad < minimo:
                minimo = cantidad
        
        cant[i] = minimo

    return reconstruir_solucion(cant, monedas)

def cambio2(monedas, monto):
    cant = [float('inf')] * (monto + 1)
    cant[0] = 0 
    monedas_usadas = [0] * (monto + 1)

    for i in range(1, monto + 1):
        for moneda in monedas:
            if moneda <= i:
                if cant[i - moneda] + 1 < cant[i]:
                    cant[i] = cant[i - moneda] + 1
                    monedas_usadas[i] = moneda
    
    # Reconstruimos la solución
    resultado = []
    i = monto
    while i > 0:
        resultado.append(monedas_usadas[i])
        i -= monedas_usadas[i]
    
    return resultado

# Ejemplo de uso
monedas = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
monto = 289

resultado = cambio2(monedas, monto)
print("Monedas usadas para dar el cambio:", resultado)