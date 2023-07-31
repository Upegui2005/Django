# Crear un login para la aplicacion, que verifique si el usuario y la contrseña son correctos
# Usuario: admin
# Clave:12345
# Darle bienvenida

cont = 0
eusuario = input("Escribe el usuario:").lower()
econtrasella = int(input("Escribe la contraseña:"))

while eusuario != "admin" and econtrasella != 12345 and cont < 2:
    cont += 1
    print("usuario o contraseña incorrecto")
    eusuario = input("Escribe el usuario:").lower()
    econtrasella = int(input("Escribe la contraseña:"))
if eusuario == "admin" and econtrasella == 12345:
    print(f"Binvenido Admin, para entrar cometiste esta cantidad de errores: {cont}")
else:
    print("No hay mas intentos")
