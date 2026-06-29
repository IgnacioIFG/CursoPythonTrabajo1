def ingresar_calificaciones():
    materias = []
    calificaciones = []
    
    while True:
        nombre_materia = input("Introduce el nombre de la materia: ").strip()
        if not nombre_materia:
            print("El nombre de la materia no puede estar vacío.")
            continue
            
        while True:
            try:
                nota_input = input(f"Introduce la calificación para {nombre_materia} (0-10): ")
                nota = float(nota_input)
                if 0 <= nota <= 10:
                    break
                else:
                    print("¡Error! La calificación debe estar entre 0.0 y 10.0.")
            except ValueError:
                print("¡Error! Debes introducir un número válido.")
        
        materias.append(nombre_materia)
        calificaciones.append(nota)
        
        continuar = input("¿Deseas introducir otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    return materias, calificaciones


def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas_indices = []
    reprobadas_indices = []
    
    for indice, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas_indices.append(indice)
        else:
            reprobadas_indices.append(indice)
            
    return aprobadas_indices, reprobadas_indices


def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
        
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)
    
    indice_max = calificaciones.index(nota_maxima)
    indice_min = calificaciones.index(nota_minima)
    
    return indice_max, indice_min


def main():
    print("=== CALCULADORA DE PROMEDIOS ESCOLARES ===")
    
    materias, calificaciones = ingresar_calificaciones()
    
    if not calificaciones:
        print("\nNo se registraron materias. El programa terminará sin datos.")
        print("¡Hasta luego!")
        return

    promedio_general = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones, umbral=5.0)
    idx_max, idx_min = encontrar_extremos(calificaciones)
    
    print("\n=======================================")
    print("           RESUMEN FINAL")
    print("=======================================")
    
    print("\n1. Todas las materias registradas:")
    for m, c in zip(materias, calificaciones):
        print(f"   - {m}: {c:.1f}")
        
    print(f"\n2. Promedio General: {promedio_general:.2f}")
    
    print("\n3. Estado de las materias:")
    print("   Aprobadas:")
    if aprobadas:
        for idx in aprobadas:
            print(f"     * {materias[idx]} ({calificaciones[idx]:.1f})")
    else:
        print("     * Ninguna")
        
    print("   Reprobadas:")
    if reprobadas:
        for idx in reprobadas:
            print(f"     * {materias[idx]} ({calificaciones[idx]:.1f})")
    else:
        print("     * Ninguna")
        
    print("\n4. Calificaciones Extremas:")
    print(f"   - Mejor materia: {materias[idx_max]} con un {calificaciones[idx_max]:.1f}")
    print(f"   - Peor materia:  {materias[idx_min]} con un {calificaciones[idx_min]:.1f}")
    
    print("\n=======================================")
    print("¡Gracias por usar la calculadora! ¡Hasta pronto!")


if __name__ == "__main__":
    main()