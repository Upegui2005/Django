n = int(input("Digite un numero positivo:"))

if n > 0:
    cont = 1
    suma = 0
    while True:
        if cont <= n:
            sueldo = int(input(f"Digite el sueldo {cont}:"))
            suma += sueldo
            pass
        else:
            break
        cont += 1

    promedio = suma / n
    print(f"El promedio de sueldos es {promedio}")
else:
    print("Debe ser mayor que cero")
