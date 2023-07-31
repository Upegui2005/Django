hora = int(input("Digita la primera hora sin minutos:"))
minutos = int(input("Digite los minutos:"))
hora2 = int(input("Digita la primera hora sin minutos:"))
minutos2 = int(input("Digite los minutos:"))

if hora > hora2:
    print(f"La primera hora digitada es mayor y es {hora}:{minutos}")
elif hora < hora2:
    print(f"La segunda hora digitada es mayor y es {hora2}:{minutos2}")
elif hora == hora2:
    if minutos > minutos2:
        print(f"La primera hora digitada es mayor y es {hora}:{minutos}")
    elif minutos < minutos2:
        print(f"La segunda hora digitada es mayor y es {hora2}:{minutos2}")
    else:
        print("Son iguales")
