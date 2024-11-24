# Solicitar los números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Solicitar la operación
operacion = input("Ingrese la operación (+, -, *, /): ")

# Realizar el cálculo correspondiente
if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de {numero1} + {numero2} es: {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de {numero1} - {numero2} es: {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de {numero1} * {numero2} es: {resultado}")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de {numero1} / {numero2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")
