puntuacion = float(input("¿Cual fue tu puntuacion?:"))

if puntuacion < 0.4:
    print("Inacetable solo recibiras $2400 y un despido")
elif puntuacion < 0.6 and puntuacion > 0.4:
    bono = (2500 * puntuacion) + 2500
    print(f"Tu puntuacion es aceptable y resiviras un bono de {bono:.0f}")
else:
    bono = (2500 * puntuacion) + 2500
    print(f"Tu puntuacion es meritoria y resiviras un bono de {bono:.0f}")
