# Solicitar la edad del usuario
edad = int(input("Por favor, ingrese su edad: "))

# Clasificar al usuario según su edad
if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif edad >= 18:
    print("Eres un adulto.")
else:
    print("La edad ingresada no es válida.")
