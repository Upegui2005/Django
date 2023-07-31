num = float(input("Escribe un numero:"))

if num >= 0:
    redondear = num + 0.5 
else:
    redondear = num - 0.5

redondear = int(redondear)
print(f"El numero es {redondear:.0f}")
