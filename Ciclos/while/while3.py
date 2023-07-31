# Averiguar el numero magico

import random

magico = random.randint(1, 10)

num = int(input("Adivina el numero del 1 - 10:"))
while num != magico:
    print("Intentalo de nuevo....")
    num = int(input("Adivina el numero del 1 - 10:"))
else:
    print("Ganaste!!")
