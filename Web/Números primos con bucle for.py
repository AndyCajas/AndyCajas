# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False  # Los números menores que 2 no son primos
    for i in range(2, int(numero ** 0.5) + 1):  # Revisa hasta la raíz cuadrada del número
        if numero % i == 0:
            return False
    return True

# Encuentra e imprime todos los números primos entre 1 y 50
print("Números primos entre 1 y 50:")
for num in range(1, 51):
    if es_primo(num):
        print(num)
