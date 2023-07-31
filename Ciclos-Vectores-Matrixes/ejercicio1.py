# Crear una lista con valores aleatorios, sin repetir ninguno.
# Los valores aleatorios van entre 1 y 50

import random

numeros = []
cont = 0
while len(numeros) < 10:
    cont += 1
    num = random.randint(1, 50)
    if num not in numeros:
        numeros.append(num)
print(numeros)
print(cont)
