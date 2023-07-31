lineasc = 183
tiempo = 45
costo = (lineasc / tiempo) * 20000
Precio = costo * 1.1 

lineasc2 = 629
tiempo2 = 200
costo2 = (lineasc2 / tiempo2) * 20000
Precio2 = costo2 * 1.1 

lineasc3 = int(input("Lineas de codigo:"))
tiempo3 = int(input("Tiempo invertido:"))
costo3 = (lineasc3 / tiempo3) * 20000
Precio3 = costo3 * 1.1 

suma = Precio + Precio2 + Precio3
print(f"El total que debe ser pagado es: {suma:.0f}")
