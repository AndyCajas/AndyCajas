# Solicita un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Variable para almacenar el número invertido
invertido = 0

# Almacena el signo del número
signo = -1 if numero < 0 else 1

# Convierte el número a positivo para trabajar con los dígitos
numero = abs(numero)

# Invierte el número usando un bucle while
while numero > 0:
    ultimo_digito = numero % 10  # Obtiene el último dígito
    invertido = invertido * 10 + ultimo_digito  # Agrega el dígito al número invertido
    numero //= 10  # Elimina el último dígito

# Restaura el signo al número invertido
invertido *= signo

print(f"El número invertido es: {invertido}")
