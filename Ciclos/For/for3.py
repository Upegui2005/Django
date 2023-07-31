# Recorrido de cadenas

# palabra = "Hola mundo, ADSO"

# for i in palabra:
# print(i)

# Averigua, cauntás vocales hay de cada una d elas palabras

frase = input("Digite una palabra: ").lower()
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0
for i in frase:
    if i == "a":
        cont_a += 1
    elif i == "e":
        cont_e += 1
    elif i == "i":
        cont_i += 1
    elif i == "o":
        cont_o += 1
    elif i == "u":
        cont_u += 1

print(f"La cantidad de:\nA: {cont_a}\nE: {cont_e}\nI: {cont_i}\nO: {cont_o}\nU: {cont_u}")
