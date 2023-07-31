cancd = int(input("¿Cuantos cd compraras?:"))

if cancd <= 9:
    pagar = cancd * 0.35
    costo = cancd * 0.25
    ganancia = pagar - (cancd * 0.25)
    print(f"El cliente debe pagar {pagar} , el costo fue de {costo} y tu ganancia fue {ganancia:.2f}")
elif cancd >= 10 and cancd <= 99:
    pagar = cancd * 0.34
    costo = cancd * 0.25
    ganancia = pagar - (cancd * 0.25)
    print(f"El cliente debe pagar {pagar:.2f} , el costo fue de {costo} y tu ganancia fue {ganancia:.2f}")
elif cancd >= 100 and cancd <= 499:
    pagar = cancd * 0.30
    costo = cancd * 0.25
    ganancia = pagar - (cancd * 0.25)
    print(f"El cliente debe pagar {pagar} , el costo fue de {costo} y tu ganancia fue {ganancia:.2f}")
else:
    pagar = cancd * 0.28
    costo = cancd * 0.25
    ganancia = pagar - (cancd * 0.25)
    print(f"El cliente debe pagar {pagar:.2f}, el costo fue de {costo} y tu ganancia fue {ganancia:.2f}")
