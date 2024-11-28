# Inicializa variables
suma_calificaciones = 0
cantidad_calificaciones = 0

print("Ingresa las calificaciones (ingresa -1 para terminar):")

while True:
    calificacion = float(input("Calificación: "))
    
    if calificacion == -1:  # Condición para terminar
        break
    
    if calificacion < 0 or calificacion > 100:  # Validación de calificación válida
        print("Por favor, ingresa una calificación válida (0-100).")
        continue
    
    suma_calificaciones += calificacion
    cantidad_calificaciones += 1

# Calcula el promedio si se ingresaron calificaciones
if cantidad_calificaciones > 0:
    promedio = suma_calificaciones / cantidad_calificaciones
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
else:
    print("\nNo se ingresaron calificaciones.")
