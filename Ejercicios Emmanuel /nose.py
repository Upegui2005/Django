num = int(input("Escribe un numero:"))

if num > 0:
    print("Es positivo")
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")
    if num % 3 == 0:
        print("Es factor de 3")
    if num ** 2 == 16:
        print("Es potencia de 2")
    if num % 10 == 7:
        print("Su residuo es 7")
    if num / 10 == 8:
        print("Su cociente es 8")
    if num >=10:
        suma = 0
        while num > 0:
            digito = num % 10
            suma += digito
            num //= 10
        if suma == 10:
            print("La suma de los numeros es 10")
else:
    print("Es Negativo")
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")
    if num % 3 == 0:
        print("Es factor de 3")
    if num ** 2 == 16:
        print("Es potencia de 2")
    if num % 10 == 7:
        print("Su residuo es 7")
    if num / 10 == 8:
        print("Su cociente es 8")
    if num >=10:
        suma = 0
        while num > 0:
            digito = num % 10
            suma += digito
            num //= 10
        if suma == 10:
            print("La suma de los numeros es 10")
