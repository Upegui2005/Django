# Construya una funcion que averigue si una persona puede votar o no, apartir de su edad

# Zona de definicion de funciones
def votar():
    print("Puedes votar")


def no_votar():
    print("No puedes votar")


# Zona del algoritmo principal -- main()
for i in range(5):
    edad = int(input("¿Cuantos años tienes?: "))
    if edad >= 18:
        votar()
    else:
        no_votar()
