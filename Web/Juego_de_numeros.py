import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Solicitar al usuario que adivine el número
adivinanza = int(input("Adivina el número entre 1 y 10: "))

# Verificar si el usuario acertó
if adivinanza == numero_aleatorio:
    print("¡Correcto! Has adivinado el número.")
else:
    print(f"Lo siento, el número correcto era {numero_aleatorio}.")
