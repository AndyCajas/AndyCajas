# Solicita un número al usuario
numero = int(input("Ingresa un número para calcular su factorial: "))

# Inicializa el factorial en 1
factorial = 1

# Calcula el factorial usando un bucle for
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {numero} es: {factorial}")
