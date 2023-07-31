print("Bienveido")

renta = float(input("¿Cuanto es tu renta anual?:"))

if renta < 10000:
    print("Debes pagar el 5%")
elif renta < 20000:
    print("Debes pagar el 15%")
elif renta < 35000:
    print("Debes pagar el 20%")
elif renta < 60000:
    print("Debes pagar el 30%")
else:
    print("Debes pagar el 45%")