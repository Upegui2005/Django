cedulas = [224524, 554541, 44541215, 55462031]
nombres = ["Emmanuel", "Andres", "Camilo", "Andrea"]
cantidadcom = [25, 33, 55, 1]
compras = []
for i in cedulas:
    buscar = int(input("Digite le numero de cedula: "))
    if i == buscar:
        print("Cliente regitrado")
        break
    else:
        print("Cliente no registrado")
        break

pregunta1 = input("¿Registrar como nuevo usuario?: ")

if pregunta1 == "si":
    print("Bienvenido al registro, a conticuacion escribe los datos correspondientes")
    cedulas.append(input("Escribe la cedula del cliente: "))
    nombres.append(input("Escribe el nombre del cliente: "))
    cantidadcom.append(int(input("Escribe las compras hechas por el cliente: ")))
else:
    print("Contiuar")

pregunta2 = input("¿Quiere comprar o ver el estado del cliente?: ").lower()

if pregunta2 == "comprar":
    print(""" Este es el menu: 
    1. Manzanas
    2. Pera
    3. Naranjas
    4. Fresas
    5. Maduros""")
    compras.append(input("Digite la cedula, producto, cantidad y precio: "))
    cantidadcom.append(1)
    print(compras)
elif pregunta2 == "estado":
    pregunta3 = int(input("Digite la cedula: "))
    while cedulas != pregunta3:
        print("A ocurrido un error")
        pregunta3 = int(input("Vuelve a digitar la cedula: "))
    else:
        print(pregunta3)
        print(cantidadcom[-1])
