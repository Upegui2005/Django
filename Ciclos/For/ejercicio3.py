import random

total = 0
cont = 0
for i in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print(f"D1:{dado1} D2:{dado2}")
    if suma == 2:
        total += 2
        break
    if suma == 12:
        continue

    total += suma
    cont += 1
else:
    print("No hubo pininis")

print(f"La suma de los dados es: {total} \nLa canrtidad de iteraciones fue: {cont}")
