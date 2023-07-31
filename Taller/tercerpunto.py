hora = int(input("Digite la hora sin minutos:"))
minutos = int(input("Digite los minutos:"))
hora2 = int(input("Digite la hora sin minutos:"))
minutos2= int(input("Digite los minutos:"))

if hora <=23 and hora <=23 and minutos <=59 and minutos2 <=59:
    if hora > hora2 or minutos > minutos2:
        print(f"La primera hora es {hora}:{minutos} la segunda es {hora2}:{minutos2} y la segunda es la menor")
    elif hora2 > hora or minutos2 > minutos:
        print(f"La primera hora es {hora}:{minutos} la segunda es {hora2}:{minutos2} y la primera es la menor")
    else:
        print(f"La primera hora es {hora}:{minutos} la segunda es {hora2}:{minutos2} y son iguales")
else:
    print("Error")