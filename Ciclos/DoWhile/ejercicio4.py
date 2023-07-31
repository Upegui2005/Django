mayor = 0
menor = 0

cont = 1
while cont <= 5:
    num = int(input(f"Digite el numero {cont}:"))
    if cont == 1:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num

        if num < menor:
            menor = num
    cont += 1
print(f"El mayor es {mayor} y el menor es {menor}")
