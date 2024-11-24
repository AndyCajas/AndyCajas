# Definir el nombre de usuario y la contraseña correctos
usuario_correcto = "admin"
contraseña_correcta = "12345"

# Contador de intentos
intentos = 0

# Solicitar el nombre de usuario y la contraseña con un máximo de 3 intentos
while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos += 1
        if intentos < 3:
            print(f"Intento fallido {intentos}/3. Vuelva a intentarlo.")
        else:
            print("Acceso bloqueado. Ha superado el número máximo de intentos.")
