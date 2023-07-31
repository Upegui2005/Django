hora = int(input("Digite la hora sin minutos: "))
minutos = int(input("Digite los minutos: "))
meridiano = input("AM o PM: ").upper()
hora2 = int(input("Digite la hora sin minutos: "))
minutos2 = int(input("Digite los minutos: "))
meridiano2 = input("AM o PM: ").upper()

if hora <=12 and hora2 <=12 and minutos <60 and minutos2 <60:
    if meridiano == "PM" and meridiano2 == "AM":
        print(f"La primera hora digitada es mayor y es: {hora}:{minutos}{meridiano}")
    elif meridiano == "AM" and meridiano2 == "PM":
        print(f"La segunda hora digitada es mayor y es: {hora2}:{minutos2}{meridiano2}")
    elif meridiano == "AM" and meridiano2 == "AM":
        if hora > hora2:
            print(f"La primera hora digitada es mayor y es: {hora}:{minutos}{meridiano}")
        elif hora2 > hora:
            print(f"La segunda hora digitada es mayor y es: {hora2}:{minutos2}{meridiano2}")
        elif hora == hora2:
            if minutos > minutos2:
                print(f"La primera hora digitada es mayor y es: {hora}:{minutos}{meridiano}")
            else:
                print(f"La segunda hora digitada es mayor y es: {hora2}:{minutos2}{meridiano2}")
    elif meridiano == "PM" and meridiano2 == "PM":
        if hora > hora2:
            print(f"La primera hora digitada es mayor y es: {hora}:{minutos}{meridiano}")
        elif hora2 > hora:
            print(f"La segunda hora digitada es mayor y es: {hora2}:{minutos2}{meridiano2}")
        elif hora == hora2:
            if minutos > minutos2:
                print(f"La primera hora digitada es mayor y es: {hora}:{minutos}{meridiano}")
            else:
                print(f"La segunda hora digitada es mayor y es: {hora2}:{minutos2}{meridiano2}")
    else:
        print("Las horas son iguales")
else:
    print("Error")
