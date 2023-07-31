# Pedir 3 edades y calcular el promedio

promedio = 0
suma = 0
for i in range(3):
    edad = int(input(f"Digite la edad {i + 1}: "))
    suma += edad

promedio = suma / 3
print(f"El promedio de las edades es: {promedio:.2f}")
