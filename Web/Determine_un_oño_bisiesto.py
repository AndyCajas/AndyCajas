# Solicitar un año al usuario
anio = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
