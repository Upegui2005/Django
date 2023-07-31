# Calcular el factorial de N

num = int(input("Digite un numero: "))

if num == 0:
    print("El factorial de 0! es: 1")
else:
    producto = 1
    for i in range(num, 0, -1):
        producto = producto * i

    print(f"El factorial de {num}! es : {producto}")
