palabra = input("Digite una palabra: ").lower()
aux = ""
for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        pass
    else:
        aux += i

print(aux)
