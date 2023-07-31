corazon = int(input("¿Cuantas veces te rompieron el corazon?:"))

if corazon == 1:
    print("Espero lo superes")
else:
    persona = input("¿Te hicieron lo mismo?:").lower()
    if persona == "si":
        print("Usted es mera gueva")
    else:
        print("Eres muy demalas")