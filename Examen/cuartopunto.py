num = int(input("Escribe un numero estre 1 y 50:"))

if num < 1 or num > 50:
    print("Deberias leer")
elif num % 8 == 0:
    if num % 5 == 0:
        print("Es multiplo de 8 y de 5")
    else:
        print("Es multiplo de 8 pero no de 5")
else:
    if num % 2 == 0:
        print("No es multiplo de 8 y es par")
    else:
        print("No es multiplo de 8 y es impar")
