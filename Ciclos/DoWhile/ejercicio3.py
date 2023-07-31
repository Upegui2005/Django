cont = 1
while cont <= 5:
    while True:
        semaforo = input(f"Digite el estado el semaforo {cont}:").lower()
        if semaforo == "rojo" or semaforo == "amarillo" or semaforo == "verde":
            break
        else:
            print("¿Si hablamos de semaforos porque dijitaste este color?")

    print(f"El color digitado fue {semaforo}")
    if semaforo == "rojo":
        print("Frena")
    elif semaforo == "amarillo":
        print("Acelere o frene")
    else:
        print("Siga su camino")
    print("Gracias por usar nuestros servicios")

    cont += 1
