# range
# for ... in
# range() funcion generadora de números en lista

#   Stop
range(5)  # Inicio en 0 y termina en 4  -> [0, 1, 2, 3, 4]
range(3)  # Inicio en 0 y termina en 2 -> [0, 1, 2]
range(1)  # Inicia en 0 y termina en 0 -> [0]
range(0)  # Inicia en - y termina - -> []

for i in range(20):
    print(i)
print(list(range(20)))
