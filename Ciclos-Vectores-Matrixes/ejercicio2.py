# Llena un vector aleatorio de 10 posiciones
# Ordenar de menor a mayor

import random

num = []
numor = []
for i in range(10):
    num.append(random.randint(20, 500))
while num:
    mayor = num[0]
    for numero in num:
        if numero < mayor:
                mayor = numero
    numor.append(mayor)
    num.remove(mayor)

print(numor)