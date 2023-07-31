# Capturas los datos personales de 3 aprendices en una matriz
# Pidiendo cedula, nombre y edad .
# Luego leer la matriz y calcular el promedio de las edades
aprendices = []

for x in range(3):
    datos = []
    ced = int(input("Digite la cedula: "))
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    datos.append(ced)
    datos.append(nombre)
    datos.append(edad)
    # Guardo todo el aprendiz completo... en aprendices
    aprendices.append(datos)

suma = 0
for i in aprendices:
    suma += i[2]

print(f"El promedio es {suma/len(aprendices):.2f}")