# Pedir por pantalla usuario y contraseña, si estan bien mostrar binvenido si no mostrar mensaje correspondiente
# Maximo 3 intentos

usuarioc = "admin"
contrasellac = 12345

for i in range(3):
    usuario = input("Escribe el usuario: ")
    contrasella = int(input("Escribe la contraseña: "))
    if usuario == usuarioc and contrasella == contrasellac:
        print("Bienvenido")
        break
    else:
        print("Usuario y contrseña incorrectos")
else:
    print("Numero de intentos agotados")
