"""
Operadores logicos 

<   Menor que 
>   Mayor que
<=  Menor o igual que 
>=  Mayor o igual que 
==  Igual, no confundir con = asignacion
!=  Diferente 
and Y
or  o
not negacion 
"""

""" 
condicion entonces 
if _______________ : 
    #bloqueo de intruscciones para el caso true 
    pass 
"""

""" 
Estructuras de control
Condicionales 
Ciclos 
Funciones 
Siempre sera en TRUE/FALSE
"""

#Boleano 

num1 = int(input("Digite un numero:"))
num2 = int(input("Digite otro numero:"))

if num1 > num2:
    print(f"El {num1} es mayor")
if num1 < num2:
    print(f"El {num2} es mayor")
else:
    print(f"{num1} y {num2} son iguales")
print("Gracias por usar el software V1.0")
