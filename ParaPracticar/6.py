nombre = input("Escribe tu nombre:").lower()
genero = input("Escribe tu genero:").lower()

if genero == "femenino":
    if nombre.lower() < "m":
        grupo = "A" 
        print(f"Tu grupo es el {grupo}")
    else:
        grupo2 = "B"
        print(f"Tu grupo es {grupo2}")
else:
    if nombre.lower() > "n":
        grupo = "A" 
        print(f"Tu grupo es el {grupo}")
    else:
        grupo2 = "B"
        print(f"Tu grupo es {grupo2}")

