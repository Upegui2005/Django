edad = int(input("¿Que edad tienes?:"))
ingresos = float(input("¿Cuanto dinero ganas?"))

if edad >=16 and ingresos >= 1000:
    print("Debes tributar")
else:
    print("No debes tributar")