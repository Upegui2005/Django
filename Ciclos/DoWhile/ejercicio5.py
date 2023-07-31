n = int(input("Digite un numero:"))

cuenta = 0
cont = 2
while cont < n:
    print(cont)
    if n % cont == 0:
        cuenta += 1
        print("No es primo")
        break

    cont += 1
if cuenta == 0:
    print("Es primo")
