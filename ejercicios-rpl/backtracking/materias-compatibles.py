def horarios_posibles(materias, solucion_parcial):
    # Si no nos quedan materias por ver
    if len(materias) == 0:
        if solucion_posible(solucion_parcial):
            return [solucion_parcial]
        else:
            return []
    # No es solucion total, pero es solucion parcial?
    if not solucion_posible(solucion_parcial):
        return []
    # Caso general, por ahora la solucion parcial es aceptada:
    materia_actual = materias.ver_primero()
    materias.borrar_primero()

    soluciones = []
    for curso in materia_actual:
        # Si es lista con soluciones, se agregan todas. Si devuelve lista vacia, no hará nada
        soluciones.extend(horarios_posibles(materias, solucion_parcial + [curso]))
    # Volver atrás un paso, para volver a poner la materia que sacamos:
    materias.guardar_primero(materia_actual)

    return soluciones
