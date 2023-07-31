def puedo_votar(e):
    if e > 17:
        print("Puede votar")
    else:
        print("No puede votar")


if __name__ == "__main__":
    for i in range(5):
        edad = int(input("¿Cuantos años tines?: "))
        puedo_votar(edad)
else:
    print("No soy yo, ejecute tal archivo.py que es el main()")

