x = int(input("Digite un numero: "))
y = int (input("Digite un numero: "))
resultado1 = x + (3*y)
resultado2 = (2 * x) - (5 * y)

if resultado1 == resultado2:
    print(f"Los resultados son {resultado1},{resultado2} y son iguales")
else:
    print(f"Los resultados son {resultado1},{resultado2} y son distintos")
