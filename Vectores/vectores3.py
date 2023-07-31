# append (Agregar valores)
edades = []
edades.append(20)
edades.append("hola")
edades.append(True)

print(edades)
print(len(edades))

# Borar ---- remove() pop() delete() clean()
import random

numeros = []
for i in range(10):
    numeros.append(random.randint(3000, 5000))
print(f"Tam de la lista: {len(numeros)}")
print(numeros)

elemento = int(input(f"Que posicion quiere eliminar 0 - {len(numeros)}: "))
numeros.pop(elemento)
print(numeros)

valor = int(input("Que valor del vector quiere eliminar?: "))
numeros.remove(valor)
print(numeros)