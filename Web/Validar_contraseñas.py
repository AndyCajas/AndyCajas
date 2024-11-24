# Definir la contraseña correcta
contraseña_correcta = "12345"

# Solicitar la contraseña al usuario
contraseña = input("Ingrese su contraseña: ")

# Validar la contraseña
if contraseña == contraseña_correcta:
    print("Contraseña correcta. Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")
