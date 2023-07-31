edad = int(input("¿Que edad tienes?:"))

if edad < 4:
    print("Entras gratis")
elif edad > 4 and edad <= 18:
    print("Debes pagar $5")
else:
    print("Debes pagar $10")