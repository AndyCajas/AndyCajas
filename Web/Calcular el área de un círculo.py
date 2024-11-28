import math

# Función que recibe el radio de un círculo y retorna su área
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2  # Fórmula del área del círculo: π * r²
    return area

# Solicitar el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área usando la función
area = calcular_area_circulo(radio)

# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area:.2f}")
