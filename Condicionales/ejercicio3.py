"""
Pedir al usuario las 3 notas del algoritmo calcular su promedio

Si el promedio es mayor o igual que 3.5, mostrar mensaje "felicidades gano"

Ademas calcular un 10% de aumento en la nota sin importar que su promedio podria ser 5.0

Si el promedio es menor entonces indicar que perdio 
"""

nota1 = float(input("Digite la primera nota:"))
nota2 = float(input("Digite la segunda nota:"))
nota3 = float(input("Digite la tercera nota:"))
promedio = (nota1 + nota2 + nota3) / 3
aumento = (promedio * 0.10) + promedio

if (aumento >= 3.5):
    print(f"Felicidades gano, su nota final fue {aumento:.1f}")
elif (promedio < 3.5):
    print(f"Perdio, tu nota final fue {promedio:.1f}")
