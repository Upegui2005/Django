"""
Construya un algoritmo que simule un semaforo

Preguntar al usuario en que color esta el semaforoy mostrar el mensaje correspondiente para cada caso
"""

color = input("Escribe el color del semaforo:")

if (color == "Verde"):
    print(f"Sigue tu camino porque esta en {color}")
elif (color == "Amarillo"):
    print(f"Empieza a detenerte o acelera porque esta en {color}")
elif (color == "Rojo"):
    print(f"Detente porque esta en {color}")
else:
    print("Tu donde haz visto un semaforo de ese color y solo falta que te pases de gueva y escribas un numero")