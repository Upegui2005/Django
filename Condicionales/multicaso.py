#Condicional completo, multicaso
"""
if _____________:
    pass
elif:
    pass
elif:
    pass   
else:
    pass
"""
#Nota: El else es el fin de los condicionales, los elif solo se ponen en la mitad y puedo omitir el else 

#Convertir un numero entre 1 y 5 a palabras 

num = int(input("Escribe un numero del 1 al 5:"))

if (num == 1):
    print("Uno")
elif (num == 2):
    print("Dos")
elif (num == 3):
    print("Tres")
elif (num == 4):
    print("Cuatro")
elif (num == 5):
    print("Cinco")
else:
    print("Para que pones ese numero si te dije de 1 a 5")
