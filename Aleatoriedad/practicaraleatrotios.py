#Juego Construya un algoritmo que lanze dos dados 4 veces. contar las veces en que la suma de ellos de 5 y 10 y ademas si hubo pinini o no.

import random
cincos = 0
diezes = 0
pinini = 0

dado = random.randint(1,6)
dado2 = random.randint(1,6)

if dado + dado2 == 5:
    cincos += 1
elif dado + dado2 == 10:
    diezes += 1
elif dado == 1 and dado2 == 1:
    pinini +=1
  

dado = random.randint(1,6)
dado2 = random.randint(1,6)

if dado + dado2 == 5:
    cincos += 1
elif dado + dado2 == 10:
    diezes += 1
elif dado == 1 and dado2 == 1:
    pinini +=1
    
dado = random.randint(1,6)
dado2 = random.randint(1,6)

if dado + dado2 == 5:
    cincos += 1
elif dado + dado2 == 10:
    diezes += 1
elif dado == 1 and dado2 == 1:
    pinini +=1

dado = random.randint(1,6)
dado2 = random.randint(1,6)

if dado + dado2 == 5:
    cincos += 1
elif dado + dado2 == 10:
    diezes += 1
elif dado == 1 and dado2 == 1:
    pinini +=1

print(f"La suma de los dados dio cinco: {cincos}, diez: {diezes} y pininis: {pinini}")