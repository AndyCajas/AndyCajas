# Solicita un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Convierte el número a positivo si es negativo
numero = abs(numero)

# Calcula la suma de los dígitos
suma_digitos = 0
while numero > 0:
    suma_digitos += numero % 10  # Obtiene el último dígito
    numero //= 10  # Elimina el último dígito

print(f"La suma de los dígitos es: {suma_digitos}")
