# Función que recibe dos números y retorna su suma
def sumar(num1, num2):
    return num1 + num2

# Bucle para solicitar pares de números y calcular su suma
while True:
    # Solicita dos números al usuario
    try:
        numero1 = float(input("Ingresa el primer número (o 'salir' para terminar): "))
        numero2 = float(input("Ingresa el segundo número: "))
        
        # Calcula y muestra la suma
        resultado = sumar(numero1, numero2)
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        print("Por favor ingresa números válidos.")
    
    # Pregunta si desea continuar o salir
    continuar = input("¿Quieres ingresar otro par de números? (sí/no): ").strip().lower()
    if continuar != "sí":
        print("¡Hasta luego!")
        break
