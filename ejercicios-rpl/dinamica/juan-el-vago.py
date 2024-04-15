# Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

# Nota sobre RPL: en este ejercicio se pide cumplir la tarea "utilizando programación dinámica". Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción

# 1. Creamos un arreglo dp de tamaño igual al número de días, inicializado con ceros.
# 2. Para cada día i, calculamos dp[i] como el máximo entre:
#       - El monto esperado a ganar ese día más el monto máximo ganado hasta el día i-2 (si existe).
#       - El monto máximo ganado hasta el día i-1.
# 3. Una vez calculado dp, reconstruimos la solución encontrando los días en los que Juan debe trabajar. Comenzamos desde el último día y retrocedemos siguiendo las mismas reglas que utilizamos para calcular dp.

def juan_el_vago(trabajos):
    n = len(trabajos)

    # DINAMICA
    if n == 0:
        return []

    dp = [0] * n
    dp[0] = trabajos[0]

    for i in range(1, n):
        dp[i] = max(trabajos[i] + (dp[i - 2] if i >= 2 else 0), dp[i - 1])

    # RECONSTRUCCION
    dias_trabajo = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            dias_trabajo.append(i)
            i -= 2
        else:
            i -= 1

    dias_trabajo.reverse()
    return dias_trabajo

# Ejemplo de uso
trabajos = [3, 2, 5, 8, 7, 6]
print(juan_el_vago(trabajos))

