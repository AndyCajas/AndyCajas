# Solicitar tres números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Determinar el mayor de los tres números
if numero1 >= numero2 and numero1 >= numero3:
    print(f"El mayor número es: {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El mayor número es: {numero2}")
else:
    print(f"El mayor número es: {numero3}")
