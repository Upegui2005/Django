"""
Construya un software que lea un numero por pantalla, si el numero es 0, se debe pedir su nombre de lo contrario pedir su apellido
"""

num1 = int(input("Digite un numero:"))

if (num1 == 0):
    input("Digite su nombre:")   
else:
   input("Digita tu apellido:")
print(f"El numero fue {num1}")
