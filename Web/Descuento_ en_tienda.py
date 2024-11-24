# Solicitar el monto gastado al cliente
monto = float(input("Por favor, ingrese el monto gastado: "))

# Calcular el monto final con o sin descuento
if monto > 100:
    descuento = monto * 0.20
    monto_final = monto - descuento
    print(f"Se aplica un descuento del 20%. El monto final es: ${monto_final:.2f}")
else:
    print(f"No se aplica descuento. El monto final es: ${monto:.2f}")
