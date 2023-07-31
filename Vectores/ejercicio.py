lista_1 = ["ma", "me", "mi", "mo", "mu"]
lista_2 = ["pa", "pe", "pi", "po", "pu"]

for i in range(len(lista_2)):
    print(f"{lista_1[i]} - {lista_2[i]} ")

for x in zip(lista_1, lista_2):
    print(x)
