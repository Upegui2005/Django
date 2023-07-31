# Crear un login para la aplicacion, que verifique si el usuario y la contrseña son correctos
# Usuario: admin
# Clave:12345
# Darle bienvenida
cont = 0
usuario = "admin"
contrasella = 12345
eusuario = input("Escribe el usuario:").lower()
econtrasella = int(input("Escribe la contraseña:"))

while eusuario != usuario or econtrasella != contrasella:
    cont += 1
    if cont > 2:
        print("No hay mas intentos")
        break
    print("usuario o contraseña incorrecto")
    eusuario = input("Escribe el usuario:").lower()
    econtrasella = int(input("Escribe la contraseña:"))
else:
    print(f"Binvenido {usuario}, para entrar cometiste esta cantidad de errores: {cont}")
