# Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.
# Las ecuaciones de recurrencia son:
# OPTLondres[n] = L[n] + min(OPTCalifornia[n-1] + M, OPTLondres[n-1])
# OPTCalifornia[n] = C[n] + min(OPTLondres[n-1] + M, OPTCalifornia[n-1])

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    OPTLondres = [0] * n
    OPTCalifornia = [0] * n
    
    OPTLondres[0] = arreglo_L[0]
    OPTCalifornia[0] = arreglo_C[0]
    
    for i in range(1, n):
        OPTLondres[i] = arreglo_L[i] + min(OPTCalifornia[i-1] + costo_M, OPTLondres[i-1])
        OPTCalifornia[i] = arreglo_C[i] + min(OPTLondres[i-1] + costo_M, OPTCalifornia[i-1])
    
    secuencia = [0] * n
    if OPTLondres[-1] < OPTCalifornia[-1]:
        secuencia[-1] = "Londres"
        ciudad_actual = "Londres"
    else:
        secuencia[-1] = "California"
        ciudad_actual = "California"
    
    # Reconstruir
    for i in range(n-2, -1, -1):
        if ciudad_actual == "Londres":
            if OPTLondres[i+1] == arreglo_L[i+1] + OPTLondres[i]:
                secuencia[i] = "Londres"
            else:
                secuencia[i] = "California"
                ciudad_actual = "California"
        else:
            if OPTCalifornia[i+1] == arreglo_C[i+1] + OPTCalifornia[i]:
                secuencia[i] = "California"
            else:
                secuencia[i] = "Londres"
                ciudad_actual = "Londres"
    
    return secuencia

# Ejemplo de uso
arreglo_L = [10, 20, 300, 40, 50]
arreglo_C = [15, 25, 35, 45, 55]
costo_M = 1

resultado = plan_operativo(arreglo_L, arreglo_C, costo_M)
print("Secuencia óptima de ciudades para operar:", resultado)
